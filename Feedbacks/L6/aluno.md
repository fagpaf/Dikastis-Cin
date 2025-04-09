# Feedback da Lista 6 - Dicionários e Tuplas

Olá, **Raissa!** Tudo bem?
Desculpe pela demora, mas fim de semestre é sempre caótico e **Parabéns** por ter concluído a Lista 6!

---

## 1. def chamar_informacoes():
Gosto da sua ideia de criar ela, mas tem um problema que é o seguinte ela faz mais do que chamar as informações na **Q1** ela **adiciona e elimina** as cidades na **Q3 registra o líder e o acontecimento**, funções devem ser criadas para realizar uma única atividade no código, isto deixa ele mais limpo e reutilizável posteriormente.

**Raissa**, mais uma vez, ***parabéns*** pelo seu esforço e dedicação! Como a cadeira acabou e você se saiu muito bem, fiz as OBS para você escrever códigos mais **elegantes**, conhecer **novos conceitos**, esclarecer uns pontos que aparentemente ainda não tinham sido **fixados**. Foi um prazer escrever seus feedbacks! Espero que tenha lido todos kk até mais.

Aqui é legal você conhecer o conceito de **Never Naste**
[***Vídeo no You Tube sobre.***](https://www.youtube.com/watch?v=CFRhGnuXG-4), vou dar um exemplo simples que você vai entender:


Aqui temos um problema visual, no qual você repete as colocações dos bairros o que acaba em poluição visual, pois as linhas estão sendo repetidas desse modo você consegue fazer tudo de uma vez só.

```python
colocados = [
    ('primeiro colocado', 'ramo primeiro colocado', 1),
    ('segundo colocado', 'ramo segundo colocado', 2),
    ('terceiro colocado', 'ramo terceiro colocado', 3)
]

populacao = resultados_bairros[bairro]['população']

for colocacao, ramo_chave, divisor in colocados:
    figura = resultados_bairros[bairro][colocacao]
    ramo = resultados_bairros[bairro][ramo_chav"~e]
    figura_ramo[figura] = ramo
    pontos = populacao // divisor
    pontuacao_impacto[figura] += pontos
    pontuacao_total[figura] += pontos
