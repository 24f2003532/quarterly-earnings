# analysis.py
# Marimo interactive notebook
# Email: 24f2003532@ds.study.iitm.ac.in

import marimo

app = marimo.App()


# ------------------------------------------
# CELL 1: Base data and widget
# ------------------------------------------
@app.cell
def __():
    import numpy as np
    import marimo as mo

    # Interactive slider controls number of data points
    n_slider = mo.ui.slider(10, 200, 10, label="Number of Samples")

    # Base dataset generator
    def generate_data(n):
        x = np.linspace(0, 10, n)
        y = 2 * x + 3 + np.random.normal(0, 2, n)
        return x, y

    n_slider  # show widget
    return generate_data, n_slider, np
# (Data flow: n_slider → generate_data)


# ------------------------------------------
# CELL 2: Derived dependent variables
# ------------------------------------------
@app.cell
def __(generate_data, n_slider):
    # Create data *dependent* on slider value
    x, y = generate_data(n_slider.value)

    # Mean values for demonstration
    x_mean = x.mean()
    y_mean = y.mean()

    x_mean, y_mean
    return x, y, x_mean, y_mean
# (Data flow: n_slider → generate_data → x,y,x_mean,y_mean)


# ------------------------------------------
# CELL 3: Dynamic Markdown based on widget
# ------------------------------------------
@app.cell
def __(mo, n_slider, x_mean, y_mean):
    mo.md(
        f"""
        ### 📊 Dynamic Summary  
        **Number of Samples:** {n_slider.value}  
        **Mean of X:** {x_mean:.2f}  
        **Mean of Y:** {y_mean:.2f}  

        The values above automatically update when the slider changes.
        """
    )
    return
# (Data flow: slider and computed fields → dynamic markdown)


# ------------------------------------------
# CELL 4: Visualization dependent on earlier cells
# ------------------------------------------
@app.cell
def __(x, y, n_slider):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6,4))
    plt.scatter(x, y, alpha=0.7)
    plt.title(f"Scatter Plot for {n_slider.value} Points")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()
    return


if __name__ == "__main__":
    app.run()
