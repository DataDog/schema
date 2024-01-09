#!/usr/bin/env python

import json
import logging
import os
import re
from typing import NamedTuple

from semantics.intake_resolved_http_span import IntakeResolvedHttpSpan
from semantics.intake_resolved_db_span import IntakeResolvedDbSpan
from semantics.intake_resolved_span import IntakeResolvedSpan
from semantics.agent_payload import AgentPayload


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def generate_schema(*args, payload_type, version_info):
    json_schema_str = json.dumps(payload_type.model_json_schema(), indent=2)
    subdir = "releases" if version_info.is_release else "drafts"

    # Create the directory if it doesn't exist
    output_dir = version_info.path
    os.makedirs(output_dir, exist_ok=True)

    snake_case_name = "".join(["_" + i.lower() if i.isupper() else i for i in payload_type.__name__]).lstrip("_")

    # Write the schema to the specified file
    # output_file = os.path.join(output_dir, "schema.json")
    output_file = os.path.join(output_dir, f"{snake_case_name}.json")
    with open(output_file, "w") as f:
        f.write(json_schema_str)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Generate schema JSON file.")
    subparsers = parser.add_subparsers(dest="command")

    # Create the parser for the "generate" command
    generate_parser = subparsers.add_parser("generate", help="Generate something")
    generate_parser.add_argument("--release", action="store_true", help="Create a new release version")
    generate_parser.add_argument(
        "--release-type",
        choices=["major", "minor", "patch"],
        default="minor",
        nargs="?",
        const="minor",
        help="Create a new release version",
    )
    args = parser.parse_args()

    if args.command == "generate":
        latest_version_info = find_latest_version()
        new_version_info = create_new_version(latest_version_info, args.release_type, args.release)
        logger.info(f"Latest version: {latest_version_info}")
        logger.info(f"New version: {new_version_info}")

        try:
            payload_types = [IntakeResolvedSpan, IntakeResolvedHttpSpan, IntakeResolvedDbSpan, AgentPayload]

            for pt in payload_types:
                generate_schema(payload_type=pt, version_info=new_version_info)

            logger.info(f"Schema successfully generated for version: {new_version_info}")
        except Exception as e:
            logger.error(f"Error generating schema: {e}")


class VersionInfo(NamedTuple):
    version: str
    path: str
    is_release: bool

    def __str__(self):
        return f"VERSION:{self.version} PATH:{self.path} ISRELEASE:{self.is_release}"


def find_latest_version(path="./../schema/releases/", is_release=True):
    """
    Looks at all the files in the provided path. Files are of the format v{semantic_version}.

    Returns: An object with the following attributes:
        - version: The semantic version.
        - path: The path to the file.
    """
    # Ensure the path ends with a slash
    if not path.endswith("/"):
        path += "/"

    # Get all files in the directory
    files = os.listdir(path)

    # Find all files that match the format v{semantic_version}
    version_files = [f for f in files if re.match("^v\d+\.\d+\.\d+$", f)]

    # If there are no matching files, return None
    if not version_files:
        return None

    # Sort the files by semantic version
    version_files.sort(key=lambda x: [int(p) for p in x[1:].split(".")])

    # The latest file is the last one in the sorted list
    latest_file = version_files[-1]

    # Extract the semantic version and path
    version = latest_file[1:]
    full_path = os.path.abspath(path + latest_file)

    return VersionInfo(version, full_path, is_release)


def create_new_version(
    last_semantic_version: VersionInfo, semantic_version_type: str, is_release: bool
) -> VersionInfo[str, str, bool]:
    """
    Determine the next semantic version number by using the provided type (patch, minor, major), and the last semantic version.

    Args:
        semantic_version_type (str): The type of semantic version update (patch, minor, major).
        last_semantic_version (VersionInfo): The last semantic version.
        is_release (bool): Whether or not this is a release.

    Returns:
        VersionInfo: A VersionInfo with the path to the new directory and the version.
    """

    major, minor, patch = map(int, last_semantic_version.version.split("."))

    if semantic_version_type == "major":
        major += 1
        minor = 0
        patch = 0
    elif semantic_version_type == "minor":
        minor += 1
        patch = 0
    elif semantic_version_type == "patch":
        patch += 1

    new_version = f"{major}.{minor}.{patch}"
    subdir = "releases" if is_release else "drafts"
    new_path = os.path.join("..", "schema", subdir, new_version)

    return VersionInfo(new_version, new_path, is_release)


if __name__ == "__main__":
    main()
