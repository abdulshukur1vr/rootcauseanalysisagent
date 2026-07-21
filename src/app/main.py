"""
CLI entry point.
"""

import argparse
import logging

from pathlib import Path


from app.pipeline import (
    RCAPipeline
)



def main():


    logging.basicConfig(

        level=logging.INFO,

        format=
        "%(asctime)s %(levelname)s %(message)s"

    )


    parser = argparse.ArgumentParser(

        description=
        "Root Cause Analysis Agent"

    )


    parser.add_argument(

        "--input",

        required=True,

        help=
        "Support bundle tar file"

    )


    parser.add_argument(

        "--output",

        default=
        "reports",

        help=
        "Report directory"

    )


    args = parser.parse_args()


    pipeline = RCAPipeline()


    pipeline.execute(

        Path(args.input),

        Path(args.output)

    )



if __name__ == "__main__":

    main()
