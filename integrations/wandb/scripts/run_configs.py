import typer
from pathlib import Path
from spacy.cli.train import train_cli

def main(ctx: typer.Context, config_dir: Path, default_config: str, results_dir: Path):
    """Run all config files instead of the default one.
    Ideally, these runs are parellellized instead of run in sequence."""
    for config_file in config_dir.iterdir():
        if config_file.name != default_config:
            output_path = results_dir / config_file.stem
            if not output_path.exists():
                output_path.mkdir()
            train_cli(ctx=ctx, config_path=config_file, output_path=output_path, code_path=None, use_gpu=-1)


if __name__ == "__main__":
    typer.run(main)
