import pandas as pd
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt

from learntools.core import *

df = pd.read_csv("../input/fifa.csv", index_col="Date", parse_dates=True)

class FeedbackSys(EqualityCheckProblem):
    _var = 'one'
    _expected = 1
    _hint = ("Quantas luas a Terra tem?")
    _solution = CS('uma só = 1')
    
class LoadFIFAData(EqualityCheckProblem):
    _var = 'fifa_data'
    _expected = df
    _hint = ("Use `pd.read_csv`, seguido pelos **três** trechos de código que "
             "estão colocados entre parênteses e separados por vírgulas. (1) O "
             "filepath para o dataset é especificado em `fifa_filepath`.  (2) Use "
             "a coluna `\"Date\"` para rotular as linhas. (3) Certifique-se de que os "
             "rótulos das linhas sejam reconhecidos como datas.")
    _solution = CS('fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)')

class PlotLine(CodingProblem):
    _var = 'plt'
    _hint = ("Consulte o tutorial para ver a solução. A linha de código que você precisa "
             " para preencher começa com `sns.lineplot`.")
    _solution = CS(
"""# Define a largura e a altura da figura
plt.figure(figsize=(16,6))

# Gráfico de linhas mostrando a evolução dos rankings da FIFA ao longo do tempo
sns.lineplot(data=fifa_data)
""")
    
    def solution_plot(self):
        self._view.solution()
        plt.figure(figsize=(16,6))
        sns.lineplot(data=df)
  
    def check(self, passed_plt):
        
        assert len(passed_plt.figure(1).axes) > 0, \
        ("Depois de escrever o código para criar um gráfico de linhas, `check()` vai revelar "
         "se seu código está correto.")
        
        main_axis = passed_plt.figure(1).axes[0]
        legend_handles = main_axis.get_legend_handles_labels()[0]
        
        assert all(isinstance(x, matplotlib.lines.Line2D) for x in legend_handles), \
        ("A sua figura é um gráfico de linhas? Por favor, use `sns.lineplot()` para gerar "
         "as linhas na sua figura.")

        assert len(legend_handles) == 6, \
        ("Sua plotagem não parece ter 6 linhas (uma linha para cada museu). "
         "Consegui detectar %d linhas.") % len(legend_handles)
        
class ThinkLine(ThoughtExperiment):
    _hint = ("Quais linhas permanecem pelo menos cinco anos consecutivos na parte inferior do gráfico?")
    _solution = ("O único país que atende a esse critério é o Brasil (code: BRA), mantendo "
                 "a posição mais alta entre 1996 e 2000. Outros países permanecem na primeira posição "
                 "por algum tempo, mas o Brasil é o único que a mantém por pelo menos cinco anos "
                 "**consecutivos**.")
        
Line = MultipartProblem(PlotLine, ThinkLine)
       
qvars = bind_exercises(globals(), [
    FeedbackSys,
    LoadFIFAData,
    Line
    ],
    var_format='step_{n}',
    )
__all__ = list(qvars)
