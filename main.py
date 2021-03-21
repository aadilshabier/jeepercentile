import matplotlib.pyplot as plt
import numpy as np
from config import starting_rank, ending_rank, \
    no_of_plots, expected_students_lower, expected_students_upper, style


def percentile(x, rank):
    return (x-rank)/x*100


def main():
    x = np.arange(expected_students_lower, expected_students_upper+1, 10_000)

    plt.style.use(style)
    for rank in np.linspace(starting_rank, ending_rank, no_of_plots):
        plt.plot(x/100_000, percentile(x, round(rank)), label=f"{round(rank)}")

    plt.title("JEE Percentile")
    plt.legend(title='Ranks', loc='upper right')
    plt.xlabel("Expected candidates (lakhs)")
    plt.ylabel("Percentile (%)")
    plt.ylim(top=100)

    plt.show()


if __name__ == "__main__":
    main()
