"""Train and run semantic diff models.

Usage:
    tell (train|evaluate) [options] PARAM_PATH
    tell (-h | --help)
    tell (-v | --version)

Options:
    -e --expt-dir EXPT_PATH
                        Directory to store experiment results and model files.
                        If not given, they will be stored in the same directory
                        as the parameter file.
    -r, --recover       Recover training from existing model.
    -f, --force    Delete existing models and logs.
    -o --overrides OVERRIDES
                        A JSON structure used to override the experiment
                        configuration.
    -u --pudb           Enable debug mode with pudb.
    -p --ptvsd PORT     Enable debug mode with ptvsd on a given port, for
                        example 5678.
    -g --file-friendly-logging
                        Outputs tqdm status on separate lines and slows tqdm
                        refresh rate
    -i --include-package PACKAGE
                        Additional packages to include.
    -q --quiet          Print less info
    -s --eval-suffix S  Evaluation generation file name [default: ]
    PARAM_PATH          Path to file describing the model parameters.
    -m --model-path PATH Path the the best model.

Examples:
    tell train -r -g expt/writing-prompts/lstm/config.yaml
"""

import os

import ptvsd
import pudb
from docopt import docopt
from schema import And, Or, Schema, Use


# from .evaluate import evaluate_from_file
from .train import train_model_from_file


# def validate(args):
#     """Validate command line arguments."""
#     args = {k.lstrip('-').lower().replace('-', '_'): v
#             for k, v in args.items()}
#     schema = Schema({
#         'param_path': Or(None, os.path.exists),
#         'model_path': Or(None, os.path.exists),
#         'ptvsd': Or(None, And(Use(int), lambda port: 1 <= port <= 65535)),
#         'eval_suffix': str,
#         object: object,
#     })
#     args = schema.validate(args)
#     args['debug'] = args['ptvsd'] or args['pudb']
#     return args


def main():
    args = {
        'train': True,
        'param_path': 'src/tell/commands/config.yaml',
        'expt_dir': 'src/tell/commands/expt/test'
    }

    if args['train']:
        train_model_from_file(
            parameter_filename=args['param_path'],
            serialization_dir=args['expt_dir'],
            force=True
            # overrides=args['overrides'],
            # file_friendly_logging=args['file_friendly_logging'],
            # recover=args['recover'],
            # force=args['force']
        )

    # elif args['evaluate']:
    #     evaluate_from_file(args['param_path'], args['model_path'],
    #                        args['overrides'], args['eval_suffix'])


if __name__ == '__main__':
    main()