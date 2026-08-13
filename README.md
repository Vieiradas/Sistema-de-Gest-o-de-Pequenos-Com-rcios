# Aprendizados
Registro dos principais conceitos, tecnologias e comandos utilizados durante o desenvolvimento do projeto.

# Tecnologias
Python | PostgreSQL | SQL | Psycopg | Git | GitHub | python-dotenv.

# Python
Variáveis | Condicionais | Loops | Funções | Importação de módulos | Input | Tratamento de erros.

# PostgreSQL / SQL
CREATE TABLE | INSERT | SELECT | UPDATE | DELETE | ALTER TABLE | PRIMARY KEY | FOREIGN KEY | UNIQUE | CREATE INDEX | ON CONFLICT | JOIN.

# Integração Python + PostgreSQL
Criação de conexão | Fechamento de conexão | cursor | execute | fetchall | commit.

# Git
Bash | git init | git status | git add | git commit -m "Initial commit" | git remote -v | git push -u origin master.

# Organização e segurança
Uso de .env | .gitignore | Separação de credenciais do código | Organização de arquivos por responsabilidade.



# Dificuldades encontradas
- Integração Python + PostgreSQL.
  
No início, a conexão apresentava problemas porque o objeto de conexão era fechado no conexao.py antes de ser utilizado pelo main.py.
  ERRO:
  psycopg2.InterfaceError: connection already closed.
  
Levou a reorganização da conexão em uma função, que permitiu que cada operação criasse sua própria conexão.
  SOLUÇÂO:
  def conectar():
      return psycopg.connect(...)



- Estrutura e consistência dos dados.

Durante os primeiros INSERTs, ocorreram erros relacionados à quantidade de colunas, valores e nomes incorretos. Isso ajudou a entender a necessidade de manter correspondência entre dados e de manter os nomes das colunas consistentes entre Python e PostgreSQL.
  ERRO:
  coluna "data_nasc" da relação "clientes" não existe.

  SOLUÇÂO:
  [AJUSTE DE NOMES E VALORES]



  - Validação de dados.

O PostgreSQL rejeitou corretamente dados inválidos, como uma data inexistente: 30-02-1998.
  ERRO:
  DatetimeFieldOverflow

  SOLUÇÂO:
  [CORREÇÂO DA DATA]

  OBSERVAÇÂO: Também foi percebida a necessidade de formatar e validar CPF, telefone, e-mail e datas antes de enviá-los ao banco.



 - Configuração do ambiente.

A configuração de credenciais também exigiu alguns ajustes, para retirar a senha do código. Foi necessário aprender a utilizar: .env | .gitignore | python-dotenv.

  OBSERVAÇÂO: Também houve problemas iniciais com o psycopg2 e com a codificação das mensagens de erro no Windows. A solução adotada foi migrar para Psycopg 3, que apresentou mensagens de erro mais claras e resolveu a comunicação com o PostgreSQL.



  - Git e Github.

No início, o Git não estava disponível no terminal e foi necessário configurar sua instalação e o PATH do Windows. Depois, também foi necessário aprender: git init, git status, git add, git commit, git remote e git push.
