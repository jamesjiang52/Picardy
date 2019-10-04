import click
import lut
import utils
import display
import play


@click.command()
@click.argument(
    "chords",
    nargs=-1,
    required=1
)
@click.option(
    "--tempo",
    "-t",
    default=60,
    help="Set the tempo, in beats per minute. Default: 60."
)
@click.option(
    "--duration",
    "-d",
    default=1,
    help="Set the duration of each chord, in beats. Default: 1."
)
def main(chords, tempo, duration):
    """Play a sequence of chords.\n
    e.g. python picardy.py Cm Ddim G7 Cm
    """
    for chord in chords:
        notes = utils.get_indices(lut.lut[utils.get_canonical_name(chord)])
        display.clear()
        display.draw_keyboard(notes)
        play.play_chord(notes, tempo, duration)


if __name__ == "__main__":
    main()
