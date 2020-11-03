def predict():
    arg_parser = argparse.ArgumentParser(add_help=False)
    args, _ = arg_parser.parse_known_args()
    arg_parser = eval_argparser()
    process_configs(target=__eval, arg_parser=arg_parser)