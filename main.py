import matplotlib.pyplot as plt
import numpy as np
from config import starting_rank, ending_rank, \
    no_of_plots, expected_students_lower, expected_students_upper, style


def percentile(x, rank):
    return (x-rank)/x*100


def main():
    x = np.arange(expected_students_lower, expected_students_upper+1, 10000)

    if style in plt.style.available:
        plt.style.use(style)
    for rank in np.linspace(starting_rank, ending_rank, no_of_plots):
        plt.plot(x/100000, percentile(x, round(rank)),
                 label="{}".format(round(rank)), linewidth=3)

    plt.title("JEE Percentile")
    plt.legend(title='Ranks', loc='upper right')
    plt.xlabel("Expected candidates (lakhs)")
    plt.ylabel("Percentile (%)")
    plt.ylim(top=100)

    plt.show()


if __name__ == "__main__":
    main()
