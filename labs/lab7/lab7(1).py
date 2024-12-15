import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 10, 500)  
y = x ** np.sin(10 * x)  


plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r"$Y(x) = x^{\sin(10x)}$", color="blue")


plt.title(r"Графік функції $Y(x) = x^{\sin(10x)}$", fontsize=14)
plt.xlabel("$x$", fontsize=12)
plt.ylabel("$Y(x)$", fontsize=12)


max_x = x[np.argmax(y)]
max_y = np.max(y)
plt.annotate('Максимум', xy=(max_x, max_y), xytext=(max_x + 1, max_y + 10),
             arrowprops=dict(facecolor='red', shrink=0.05), fontsize=10)


plt.text(2, 50, "Цікава поведінка функції", fontsize=10, color="green")


plt.figtext(0.1, 0.9, "2D графік функції", fontsize=12, color="purple")


plt.legend(fontsize=12, loc="upper right")


plt.savefig("2d_graph_function.png", format="png", dpi=300)
print("Графік збережено як 2d_graph_function.png")


plt.show()  