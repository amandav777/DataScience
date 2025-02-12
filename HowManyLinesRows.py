import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# ???
np.set_printoptions(suppress=True)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
sns.set_theme()



# nome do arquivo
file_name = "/content/enhanced_box_office_data(2000-2024)u.csv"

# formar a tabela
df = pd.read_csv(file_name)

#qtd linhas e colunas. o metodo shape conta linhas e colunas
print(df.shape)