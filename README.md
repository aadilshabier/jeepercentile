# JEE Percentile Visualizer

A simple project to visualize your JEE percentile for different ranks and plot them against the number of students writing the exam for different expected scores.

### Prerequisites

- Basic knowledge of python

- python3

- numpy

  ```shell
  $ pip install numpy
  ```

- matplotlib

  ```shell
  $ pip install matplotlib
  ```

### Usage

1. Open `config.py` in a text editor.

2. Change the values of these constants to your liking.

   - **starting_rank**: Rank to start plotting from.
   - **ending_rank**: Rank to end plotting at.
   - **no_of_plots**: Number of plots between starting and ending rank.
   - **expected_students_lower**: Lower bound of candidates expected to write the exam.
   - **expected_students_upper**: Upper bound of candidates expected to write the exam.

3. Run `main.py` using:
   1. IDLE
   2. Command line (python should be in PATH)  
      Go to the directory of `main.py`
   ```shell
   $ python main.py
   ```
