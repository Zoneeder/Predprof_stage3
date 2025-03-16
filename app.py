import matplotlib.pyplot as plt
import numpy as np
from flask import *

app = Flask(__name__)


# Главная страница с отображением продуктов конкретного пользователя
@app.route('/')
def home():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)

# plt.style.use('_mpl-gallery-nogrid')

# # make data
# X, Y = np.meshgrid(np.linspace(-3, 3, 16), np.linspace(-3, 3, 16))
# Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)

# # plot
# fig, ax = plt.subplots()

# ax.imshow(Z, origin='lower')
# plt.show()