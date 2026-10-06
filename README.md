1. Por que usamos um ambiente virtual em cada projeto?
Isolamos o ambiente Python do projeto para instalar as dependências (como o Django) de forma organizada. Isso evita que as bibliotecas deste sistema se misturem com o Python global do computador ou com outros projetos, garantindo que o sistema funcione com as versões corretas.

2. Por que dividimos o sistema em 3 apps em vez de um só?
Dividimos o sistema em múltiplos apps para que cada um cuide de uma responsabilidade específica de forma lógica. Cada módulo (como alunos, disciplinas e avaliações) possui seus próprios arquivos de models, views e rotas, o que mantém o código organizado e fácil de manter.

3. Para que servem makemigrations e migrate, e por que nessa ordem?
O makemigrations funciona como um "planejador": ele analisa as alterações feitas nos arquivos de banco de dados (models.py) e gera arquivos de instruções detalhadas. O migrate funciona como o "executor": ele pega essas instruções que foram geradas e as aplica de fato no banco de dados físico, criando as tabelas. A ordem é obrigatória porque não é possível executar as alterações sem antes planejá-las e traduzi-las.