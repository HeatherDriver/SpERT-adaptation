import argparse

from .args import train_argparser, eval_argparser
from .config_reader import process_configs
from .src import input_reader
from .src.spert_trainer import SpERTTrainer


def __eval(run_args):
    trainer = SpERTTrainer(run_args)
    trainer.eval(dataset_path=run_args.dataset_path, types_path=run_args.types_path,
                 input_reader_cls=input_reader.JsonInputReader)


def _eval():
    arg_parser = eval_argparser()
    process_configs(target=__eval, arg_parser=arg_parser)


def predict():
    arg_parser = argparse.ArgumentParser(add_help=False)
    args, _ = arg_parser.parse_known_args()
    _eval()