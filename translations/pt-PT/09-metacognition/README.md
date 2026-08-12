[![Multi-Agente Design](../../../translated_images/pt-PT/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Clique na imagem acima para ver o vídeo desta lição)_
# Metacognição em Agentes de IA

## Introdução

Bem-vindo à lição sobre metacognição em agentes de IA! Este capítulo foi concebido para iniciantes que têm curiosidade sobre como os agentes de IA podem refletir sobre os seus próprios processos de pensamento. No final desta lição, compreenderá os conceitos chave e estará preparado com exemplos práticos para aplicar a metacognição no design de agentes de IA.

## Objetivos de Aprendizagem

Após completar esta lição, será capaz de:

1. Compreender as implicações dos ciclos de raciocínio nas definições de agentes.
2. Usar técnicas de planeamento e avaliação para ajudar agentes autocorretivos.
3. Criar os seus próprios agentes capazes de manipular código para realizar tarefas.

## Introdução à Metacognição

Metacognição refere-se a processos cognitivos de ordem superior que envolvem pensar sobre o próprio pensamento. Para agentes de IA, isto significa ser capaz de avaliar e ajustar as suas ações com base na autoconsciência e em experiências passadas. Metacognição, ou "pensar sobre pensar", é um conceito importante no desenvolvimento de sistemas de IA agentes. Envolve sistemas de IA estarem conscientes dos seus próprios processos internos e serem capazes de monitorizar, regular e adaptar o seu comportamento em conformidade. Tal como fazemos quando percebemos o ambiente ou analisamos um problema. Esta autoconsciência pode ajudar os sistemas de IA a tomar melhores decisões, identificar erros e melhorar o seu desempenho ao longo do tempo - novamente relacionando-se com o teste de Turing e o debate sobre se a IA irá assumir o controlo.

No contexto dos sistemas de IA agentes, a metacognição pode ajudar a resolver vários desafios, tais como:
- Transparência: Assegurar que os sistemas de IA podem explicar o seu raciocínio e decisões.
- Raciocínio: Melhorar a capacidade dos sistemas de IA para sintetizar informação e tomar decisões sólidas.
- Adaptação: Permitir que os sistemas de IA se ajustem a novos ambientes e condições em mudança.
- Perceção: Melhorar a precisão dos sistemas de IA no reconhecimento e interpretação de dados do seu ambiente.

### O que é Metacognição?

Metacognição, ou "pensar sobre pensar", é um processo cognitivo de ordem superior que envolve autoconsciência e autorregulação dos próprios processos cognitivos. No domínio da IA, a metacognição capacita os agentes a avaliar e adaptar as suas estratégias e ações, conduzindo a uma melhoria na capacidade de resolver problemas e tomar decisões. Ao compreender a metacognição, pode conceber agentes de IA que não são apenas mais inteligentes, mas também mais adaptáveis e eficientes. Na verdadeira metacognição, veria a IA a raciocinar explicitamente sobre o seu próprio raciocínio.

Exemplo: "Priorizei voos mais baratos porque... Posso estar a perder voos diretos, por isso vou verificar novamente.".
Acompanhar como ou porque escolheu uma determinada rota.
- Notar que cometeu erros porque confiou em excesso nas preferências do utilizador da última vez, pelo que modifica a sua estratégia de decisão e não apenas a recomendação final.
- Diagnosticar padrões como, "Sempre que vejo o utilizador mencionar 'muito cheio', não devo apenas remover certas atrações, mas também refletir que o meu método de selecionar 'principais atrações' é falho se eu sempre as ordenar por popularidade."

### Importância da Metacognição em Agentes de IA

A metacognição desempenha um papel crucial no design de agentes de IA por várias razões:

![Importância da Metacognição](../../../translated_images/pt-PT/importance-of-metacognition.b381afe9aae352f7.webp)

- Autorreflexão: Os agentes podem avaliar o seu próprio desempenho e identificar áreas para melhoria.
- Adaptabilidade: Os agentes podem modificar as suas estratégias com base em experiências passadas e ambientes em mudança.
- Correção de Erros: Os agentes podem detetar e corrigir erros autonomamente, levando a resultados mais precisos.
- Gestão de Recursos: Os agentes podem otimizar o uso de recursos, como tempo e poder computacional, planeando e avaliando as suas ações.

## Componentes de um Agente de IA

Antes de mergulhar nos processos metacognitivos, é essencial compreender os componentes básicos de um agente de IA. Um agente de IA tipicamente consiste em:

- Persona: A personalidade e características do agente, que definem como interage com os utilizadores.
- Ferramentas: As capacidades e funções que o agente pode executar.
- Competências: O conhecimento e expertise que o agente possui.

Estes componentes trabalham em conjunto para criar uma "unidade de especialização" que pode realizar tarefas específicas.

**Exemplo**:
Considere um agente de viagens, um serviço de agente que não só planeia suas férias mas também ajusta o seu percurso com base em dados em tempo real e experiências passadas dos clientes.

### Exemplo: Metacognição num Serviço de Agente de Viagens

Imagine que está a conceber um serviço de agente de viagens potenciado por IA. Este agente, "Agente de Viagens", ajuda os utilizadores a planear as suas férias. Para incorporar metacognição, o Agente de Viagens precisa de avaliar e ajustar as suas ações com base na autoconsciência e experiências passadas. Eis como a metacognição poderia desempenhar um papel:

#### Tarefa Atual

A tarefa atual é ajudar um utilizador a planear uma viagem a Paris.

#### Passos para Completar a Tarefa

1. **Recolher Preferências do Utilizador**: Perguntar ao utilizador sobre datas de viagem, orçamento, interesses (e.g., museus, gastronomia, compras) e quaisquer requisitos específicos.
2. **Obter Informação**: Procurar opções de voos, alojamento, atrações e restaurantes que correspondam às preferências do utilizador.
3. **Gerar Recomendações**: Fornecer um itinerário personalizado com detalhes dos voos, reservas de hotel e atividades sugeridas.
4. **Ajustar com Base no Feedback**: Pedir ao utilizador feedback sobre as recomendações e fazer os ajustes necessários.

#### Recursos Necessários

- Acesso a bases de dados de reservas de voos e hotéis.
- Informação sobre atrações e restaurantes em Paris.
- Dados de feedback do utilizador de interações anteriores.

#### Experiência e Autorreflexão

O Agente de Viagens usa metacognição para avaliar o seu desempenho e aprender com experiências passadas. Por exemplo:

1. **Análise de Feedback do Utilizador**: O Agente de Viagens revê o feedback para determinar quais recomendações foram bem recebidas e quais não foram, ajustando as sugestões futuras em conformidade.
2. **Adaptabilidade**: Se um utilizador mencionou anteriormente aversão a locais demasiado cheios, o Agente de Viagens evitará recomendar locais turísticos populares durante as horas de pico no futuro.
3. **Correção de Erros**: Se o Agente de Viagens cometeu um erro numa reserva passada, como sugerir um hotel lotado, aprende a verificar a disponibilidade de forma mais rigorosa antes de fazer recomendações.

#### Exemplo Prático para Programadores

Eis um exemplo simplificado de como o código do Agente de Viagens poderia ser ao incorporar metacognição:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Pesquisar voos, hotéis e atrações com base nas preferências
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # Analisar o feedback e ajustar recomendações futuras
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Exemplo de utilização
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### Por Que a Metacognição Importa

- **Autorreflexão**: Os agentes podem analisar o seu desempenho e identificar áreas para melhoria.
- **Adaptabilidade**: Os agentes podem modificar estratégias com base no feedback e condições em mudança.
- **Correção de Erros**: Os agentes podem detetar e corrigir autonomamente os erros.
- **Gestão de Recursos**: Os agentes podem otimizar o uso dos recursos, como tempo e força computacional.

Ao incorporar metacognição, o Agente de Viagens pode fornecer recomendações de viagem mais personalizadas e precisas, melhorando a experiência geral do utilizador.

---

## 2. Planeamento em Agentes

O planeamento é um componente crítico do comportamento de um agente de IA. Envolve a definição dos passos necessários para alcançar um objetivo, considerando o estado atual, recursos e possíveis obstáculos.

### Elementos do Planeamento

- **Tarefa Atual**: Definir claramente a tarefa.
- **Passos para Completar a Tarefa**: Dividir a tarefa em passos geríveis.
- **Recursos Necessários**: Identificar os recursos necessários.
- **Experiência**: Utilizar experiências passadas para informar o planeamento.

**Exemplo**:
Eis os passos que o Agente de Viagens precisa seguir para auxiliar eficazmente um utilizador a planear a sua viagem:

### Passos para o Agente de Viagens

1. **Recolher Preferências do Utilizador**
   - Perguntar ao utilizador detalhes sobre datas de viagem, orçamento, interesses e quaisquer requisitos específicos.
   - Exemplos: "Quando planeia viajar?" "Qual é o seu orçamento?" "Que atividades gosta de fazer nas férias?"

2. **Obter Informação**
   - Procurar opções de viagem relevantes baseadas nas preferências do utilizador.
   - **Voos**: Procurar voos disponíveis dentro do orçamento e datas preferidas.
   - **Alojamentos**: Encontrar hotéis ou propriedades que correspondam às preferências do utilizador em relação a localização, preço e comodidades.
   - **Atrações e Restaurantes**: Identificar atrações populares, atividades e opções gastronómicas que alinhem com os interesses do utilizador.

3. **Gerar Recomendações**
   - Compilar a informação obtida num itinerário personalizado.
   - Fornecer detalhes como opções de voo, reservas de hotel e atividades sugeridas, adequando as recomendações às preferências do utilizador.

4. **Apresentar Itinerário ao Utilizador**
   - Partilhar o itinerário proposto para revisão do utilizador.
   - Exemplo: "Aqui está um itinerário sugerido para a sua viagem a Paris. Inclui detalhes dos voos, reservas de hotel e uma lista de atividades e restaurantes recomendados. Diga-me o que pensa!"

5. **Recolher Feedback**
   - Pedir ao utilizador feedback sobre o itinerário proposto.
   - Exemplos: "Gosta das opções de voo?" "O hotel é adequado às suas necessidades?" "Há alguma atividade que gostaria de adicionar ou remover?"

6. **Ajustar com Base no Feedback**
   - Modificar o itinerário com base no feedback do utilizador.
   - Fazer as alterações necessárias nas recomendações de voo, alojamento e atividades para melhor corresponder às preferências do utilizador.

7. **Confirmação Final**
   - Apresentar o itinerário atualizado para confirmação final do utilizador.
   - Exemplo: "Fiz as alterações com base no seu feedback. Aqui está o itinerário atualizado. Está tudo do seu agrado?"

8. **Reservar e Confirmar Reservas**
   - Depois de o utilizador aprovar o itinerário, proceder à reserva de voos, alojamentos e quaisquer atividades pré-planeadas.
   - Enviar detalhes de confirmação ao utilizador.

9. **Fornecer Suporte Contínuo**
   - Manter-se disponível para ajudar o utilizador com quaisquer alterações ou pedidos adicionais antes e durante a viagem.
   - Exemplo: "Se precisar de qualquer ajuda adicional durante a sua viagem, não hesite em contactar-me a qualquer momento!"

### Exemplo de Interação

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Exemplo de uso num pedido de reserva
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

## 3. Sistema RAG Corretivo

Primeiro, vamos começar por entender a diferença entre Ferramenta RAG e Carregamento Preemptivo de Contexto

![RAG vs Carregamento de Contexto](../../../translated_images/pt-PT/rag-vs-context.9eae588520c00921.webp)

### Geração Aumentada por Recuperação (RAG)

RAG combina um sistema de recuperação com um modelo generativo. Quando é feita uma consulta, o sistema de recuperação busca documentos ou dados relevantes de uma fonte externa e essa informação obtida é usada para aumentar a entrada do modelo generativo. Isto ajuda o modelo a gerar respostas mais precisas e contextualmente relevantes.

Num sistema RAG, o agente recupera informação relevante de uma base de conhecimento e usa-a para gerar respostas ou ações apropriadas.

### Abordagem RAG Corretiva

A abordagem RAG Corretiva foca-se em usar técnicas RAG para corrigir erros e melhorar a precisão dos agentes de IA. Isto envolve:

1. **Técnica de Prompt**: Usar prompts específicos para guiar o agente na recuperação de informação relevante.
2. **Ferramenta**: Implementar algoritmos e mecanismos que permitem ao agente avaliar a relevância da informação recuperada e gerar respostas precisas.
3. **Avaliação**: Avaliar continuamente o desempenho do agente e fazer ajustes para melhorar a sua precisão e eficiência.

#### Exemplo: RAG Corretiva num Agente de Pesquisa

Considere um agente de pesquisa que recupera informação da web para responder a consultas dos utilizadores. A abordagem RAG Corretiva poderia envolver:

1. **Técnica de Prompt**: Formular consultas de pesquisa com base na entrada do utilizador.
2. **Ferramenta**: Usar processamento de linguagem natural e algoritmos de aprendizagem automática para ordenar e filtrar os resultados da pesquisa.
3. **Avaliação**: Analisar o feedback dos utilizadores para identificar e corrigir imprecisões na informação recuperada.

### RAG Corretiva no Agente de Viagens

A RAG Corretiva (Geração Aumentada por Recuperação) melhora a capacidade de uma IA para recuperar e gerar informação, corrigindo quaisquer imprecisões. Vamos ver como o Agente de Viagens pode usar a abordagem RAG Corretiva para fornecer recomendações de viagem mais precisas e relevantes.

Isto envolve:

- **Técnica de Prompt:** Usar prompts específicos para guiar o agente na recuperação de informação relevante.
- **Ferramenta:** Implementar algoritmos e mecanismos que permitam ao agente avaliar a relevância da informação recuperada e gerar respostas precisas.
- **Avaliação:** Avaliar continuamente o desempenho do agente e fazer ajustes para melhorar a sua precisão e eficiência.

#### Passos para Implementar a RAG Corretiva no Agente de Viagens

1. **Interação Inicial com o Utilizador**
   - O Agente de Viagens recolhe as preferências iniciais do utilizador, como destino, datas de viagem, orçamento e interesses.
   - Exemplo:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Recuperação de Informação**
   - O Agente de Viagens recupera informação sobre voos, alojamentos, atrações e restaurantes com base nas preferências do utilizador.
   - Exemplo:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Geração de Recomendações Iniciais**
   - O Agente de Viagens usa a informação recuperada para gerar um itinerário personalizado.
   - Exemplo:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Recolha de Feedback do Utilizador**
   - O Agente de Viagens pergunta ao utilizador sobre as recomendações iniciais.
   - Exemplo:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Processo RAG Corretivo**
   - **Técnica de Prompt**: O Agente de Viagens formula novas consultas de pesquisa com base no feedback do utilizador.
     - Exemplo:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Ferramenta**: O Agente de Viagens usa algoritmos para ordenar e filtrar novos resultados de pesquisa, enfatizando a relevância com base no feedback do utilizador.
     - Exemplo:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Avaliação**: O Agente de Viagens avalia continuamente a relevância e precisão das suas recomendações, analisando o feedback do utilizador e fazendo os ajustes necessários.
     - Exemplo:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### Exemplo Prático

Eis um exemplo simplificado em Python que incorpora a abordagem RAG Corretiva no Agente de Viagens:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)
        new_itinerary = self.generate_recommendations()
        return new_itinerary

# Exemplo de uso
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
new_itinerary = travel_agent.adjust_based_on_feedback(feedback)
print("Updated Itinerary:", new_itinerary)
```

### Carregamento Preemptivo de Contexto


O Carregamento Preemptivo de Contexto envolve carregar contexto relevante ou informação de fundo no modelo antes de processar uma consulta. Isto significa que o modelo tem acesso a esta informação desde o início, o que pode ajudá-lo a gerar respostas mais informadas sem precisar de obter dados adicionais durante o processo.

Aqui está um exemplo simplificado de como um carregamento preemptivo de contexto pode parecer para uma aplicação de agente de viagens em Python:

```python
class TravelAgent:
    def __init__(self):
        # Pré-carregar destinos populares e as suas informações
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Buscar informações do destino a partir do contexto pré-carregado
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Exemplo de utilização
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Explicação

1. **Inicialização (método `__init__`)**: A classe `TravelAgent` pré-carrega um dicionário contendo informação sobre destinos populares como Paris, Tóquio, Nova Iorque e Sydney. Este dicionário inclui detalhes como o país, moeda, idioma e principais atrações de cada destino.

2. **Obtenção de Informação (método `get_destination_info`)**: Quando um utilizador faz uma consulta sobre um destino específico, o método `get_destination_info` busca a informação relevante do dicionário de contexto pré-carregado.

Ao pré-carregar o contexto, a aplicação do agente de viagens pode responder rapidamente às consultas dos utilizadores sem ter de obter esta informação de uma fonte externa em tempo real. Isto torna a aplicação mais eficiente e responsiva.

### Inicializar o Plano com um Objetivo Antes de Iterar

Inicializar um plano com um objetivo envolve começar com um objetivo claro ou resultado pretendido em mente. Ao definir este objetivo desde o início, o modelo pode usá-lo como um princípio orientador ao longo do processo iterativo. Isto ajuda a garantir que cada iteração se aproxima do resultado desejado, tornando o processo mais eficiente e focado.

Aqui está um exemplo de como pode inicializar um plano de viagem com um objetivo antes de iterar para um agente de viagens em Python:

### Cenário

Um agente de viagens quer planear férias personalizadas para um cliente. O objetivo é criar um itinerário de viagem que maximize a satisfação do cliente com base nas suas preferências e orçamento.

### Passos

1. Definir as preferências e orçamento do cliente.
2. Inicializar o plano inicial com base nestas preferências.
3. Iterar para refinar o plano, otimizando para a satisfação do cliente.

#### Código Python

```python
class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def bootstrap_plan(self, preferences, budget):
        plan = []
        total_cost = 0

        for destination in self.destinations:
            if total_cost + destination['cost'] <= budget and self.match_preferences(destination, preferences):
                plan.append(destination)
                total_cost += destination['cost']

        return plan

    def match_preferences(self, destination, preferences):
        for key, value in preferences.items():
            if destination.get(key) != value:
                return False
        return True

    def iterate_plan(self, plan, preferences, budget):
        for i in range(len(plan)):
            for destination in self.destinations:
                if destination not in plan and self.match_preferences(destination, preferences) and self.calculate_cost(plan, destination) <= budget:
                    plan[i] = destination
                    break
        return plan

    def calculate_cost(self, plan, new_destination):
        return sum(destination['cost'] for destination in plan) + new_destination['cost']

# Exemplo de uso
destinations = [
    {"name": "Paris", "cost": 1000, "activity": "sightseeing"},
    {"name": "Tokyo", "cost": 1200, "activity": "shopping"},
    {"name": "New York", "cost": 900, "activity": "sightseeing"},
    {"name": "Sydney", "cost": 1100, "activity": "beach"},
]

preferences = {"activity": "sightseeing"}
budget = 2000

travel_agent = TravelAgent(destinations)
initial_plan = travel_agent.bootstrap_plan(preferences, budget)
print("Initial Plan:", initial_plan)

refined_plan = travel_agent.iterate_plan(initial_plan, preferences, budget)
print("Refined Plan:", refined_plan)
```

#### Explicação do Código

1. **Inicialização (método `__init__`)**: A classe `TravelAgent` é inicializada com uma lista de destinos potenciais, cada um com atributos como nome, custo e tipo de atividade.

2. **Inicializar o Plano (`bootstrap_plan` método)**: Este método cria um plano de viagem inicial baseado nas preferências e orçamento do cliente. Ele percorre a lista de destinos e adiciona-os ao plano se corresponderem às preferências do cliente e se estiverem dentro do orçamento.

3. **Correspondência de Preferências (`match_preferences` método)**: Este método verifica se um destino corresponde às preferências do cliente.

4. **Iterar o Plano (`iterate_plan` método)**: Este método refina o plano inicial tentando substituir cada destino no plano por uma melhor correspondência, considerando as preferências do cliente e as restrições do orçamento.

5. **Calcular Custo (`calculate_cost` método)**: Este método calcula o custo total do plano atual, incluindo um novo destino potencial.

#### Exemplo de Uso

- **Plano Inicial**: O agente de viagens cria um plano inicial com base nas preferências do cliente para turismo e um orçamento de 2000 dólares.
- **Plano Refinado**: O agente de viagens itera o plano, otimizando para as preferências e orçamento do cliente.

Ao inicializar o plano com um objetivo claro (por exemplo, maximizar a satisfação do cliente) e iterar para refinar o plano, o agente de viagens pode criar um itinerário personalizado e otimizado para o cliente. Esta abordagem assegura que o plano de viagem está alinhado com as preferências e orçamento do cliente desde o início e melhora-se a cada iteração.

### Tirar Proveito dos LLM para Reordenação e Pontuação

Modelos de Linguagem Grande (LLMs) podem ser usados para reordenar e classificar ao avaliar a relevância e qualidade de documentos recuperados ou respostas geradas. Aqui está como funciona:

**Recuperação:** O passo inicial de recuperação obtém um conjunto de documentos ou respostas candidatas com base na consulta.

**Reordenação:** O LLM avalia estes candidatos e reordena-os com base na sua relevância e qualidade. Este passo assegura que a informação mais relevante e de maior qualidade é apresentada primeiro.

**Pontuação:** O LLM atribui pontuações a cada candidato, refletindo a sua relevância e qualidade. Isto ajuda a selecionar a melhor resposta ou documento para o utilizador.

Ao aproveitar os LLMs para reordenação e pontuação, o sistema pode fornecer informação mais precisa e contextualizada, melhorando a experiência geral do utilizador.

Aqui está um exemplo de como um agente de viagens pode usar um Modelo de Linguagem Grande (LLM) para reordenar e pontuar destinos de viagem com base nas preferências do utilizador em Python:

#### Cenário - Viagem com base em Preferências

Um agente de viagens quer recomendar os melhores destinos de viagem a um cliente com base nas suas preferências. O LLM ajudará a reordenar e pontuar os destinos para assegurar que as opções mais relevantes são apresentadas.

#### Passos:

1. Recolher as preferências do utilizador.
2. Recuperar uma lista de destinos de viagem potenciais.
3. Usar o LLM para reordenar e pontuar os destinos com base nas preferências do utilizador.

Aqui está como pode atualizar o exemplo anterior para usar os Serviços Azure OpenAI:

#### Requisitos

1. Precisa de ter uma subscrição Azure.
2. Criar um recurso Azure OpenAI e obter a sua chave API.

#### Exemplo de Código Python

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Gere um prompt para o Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Defina cabeçalhos e payload para o pedido
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Chame a API do Azure OpenAI para obter os destinos reordenados e pontuados
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Extraia e devolva as recomendações
        recommendations = response_data['choices'][0]['text'].strip().split('\n')
        return recommendations

    def generate_prompt(self, preferences):
        prompt = "Here are the travel destinations ranked and scored based on the following user preferences:\n"
        for key, value in preferences.items():
            prompt += f"{key}: {value}\n"
        prompt += "\nDestinations:\n"
        for destination in self.destinations:
            prompt += f"- {destination['name']}: {destination['description']}\n"
        return prompt

# Exemplo de utilização
destinations = [
    {"name": "Paris", "description": "City of lights, known for its art, fashion, and culture."},
    {"name": "Tokyo", "description": "Vibrant city, famous for its modernity and traditional temples."},
    {"name": "New York", "description": "The city that never sleeps, with iconic landmarks and diverse culture."},
    {"name": "Sydney", "description": "Beautiful harbour city, known for its opera house and stunning beaches."},
]

preferences = {"activity": "sightseeing", "culture": "diverse"}
api_key = 'your_azure_openai_api_key'
endpoint = 'https://your-endpoint.com/openai/deployments/your-deployment-name/completions?api-version=2022-12-01'

travel_agent = TravelAgent(destinations)
recommendations = travel_agent.get_recommendations(preferences, api_key, endpoint)
print("Recommended Destinations:")
for rec in recommendations:
    print(rec)
```

#### Explicação do Código - Gestor de Preferências

1. **Inicialização**: A classe `TravelAgent` é inicializada com uma lista de destinos de viagem potenciais, cada um com atributos como nome e descrição.

2. **Obter Recomendações (método `get_recommendations`)**: Este método gera um prompt para o serviço Azure OpenAI com base nas preferências do utilizador e faz um pedido HTTP POST para a API Azure OpenAI para obter destinos reordenados e pontuados.

3. **Gerar Prompt (método `generate_prompt`)**: Este método constrói um prompt para o Azure OpenAI, incluindo as preferências do utilizador e a lista de destinos. O prompt orienta o modelo a reordenar e pontuar os destinos com base nas preferências fornecidas.

4. **Chamada API**: A biblioteca `requests` é usada para fazer um pedido HTTP POST ao endpoint da API Azure OpenAI. A resposta contém os destinos reordenados e pontuados.

5. **Exemplo de Uso**: O agente de viagens recolhe as preferências do utilizador (por exemplo, interesse em turismo e cultura diversa) e usa o serviço Azure OpenAI para obter recomendações reordenadas e pontuadas para destinos de viagem.

Certifique-se de substituir `your_azure_openai_api_key` pela sua chave API Azure OpenAI real e `https://your-endpoint.com/...` pelo URL do endpoint real do seu deployment Azure OpenAI.

Ao aproveitar o LLM para reordenação e pontuação, o agente de viagens pode fornecer recomendações de viagem mais personalizadas e relevantes aos clientes, melhorando a experiência global.

### RAG: Técnica de Prompting vs Ferramenta

A Geração Aumentada por Recuperação (RAG) pode ser tanto uma técnica de prompting como uma ferramenta no desenvolvimento de agentes IA. Compreender a distinção entre os dois pode ajudá-lo a tirar melhor proveito da RAG nos seus projetos.

#### RAG como Técnica de Prompting

**O que é?**

- Como técnica de prompting, a RAG envolve formular consultas ou prompts específicos para guiar a recuperação de informação relevante de um grande corpus ou base de dados. Esta informação é depois usada para gerar respostas ou ações.

**Como funciona:**

1. **Formular Prompts**: Criar prompts ou consultas bem estruturadas baseadas na tarefa ou na entrada do utilizador.
2. **Recuperar Informação**: Usar os prompts para procurar dados relevantes de uma base de conhecimento pré-existente ou conjunto de dados.
3. **Gerar Resposta**: Combinar a informação recuperada com modelos de IA generativos para produzir uma resposta abrangente e coerente.

**Exemplo no Agente de Viagens**:

- Entrada do Utilizador: "Quero visitar museus em Paris."
- Prompt: "Encontra os melhores museus em Paris."
- Informação Recuperada: Detalhes sobre o Museu do Louvre, Musée d'Orsay, etc.
- Resposta Gerada: "Aqui estão alguns dos melhores museus em Paris: Museu do Louvre, Musée d'Orsay e Centro Pompidou."

#### RAG como Ferramenta

**O que é?**

- Como ferramenta, a RAG é um sistema integrado que automatiza o processo de recuperação e geração, facilitando a implementação de funcionalidades complexas de IA pelos desenvolvedores sem ter que criar manualmente prompts para cada consulta.

**Como funciona:**

1. **Integração**: Incorpora a RAG na arquitetura do agente de IA, permitindo que este trate automaticamente as tarefas de recuperação e geração.
2. **Automação**: A ferramenta gere todo o processo, desde receber a entrada do utilizador até gerar a resposta final, sem necessidade de prompts explícitos para cada passo.
3. **Eficiência**: Melhora o desempenho do agente ao agilizar o processo de recuperação e geração, permitindo respostas mais rápidas e precisas.

**Exemplo no Agente de Viagens**:

- Entrada do Utilizador: "Quero visitar museus em Paris."
- Ferramenta RAG: Recupera automaticamente informação sobre museus e gera uma resposta.
- Resposta Gerada: "Aqui estão alguns dos melhores museus em Paris: Museu do Louvre, Musée d'Orsay e Centro Pompidou."

### Comparação

| Aspeto                  | Técnica de Prompting                                     | Ferramenta                                             |
|-------------------------|----------------------------------------------------------|--------------------------------------------------------|
| **Manual vs Automático**| Formula manual de prompts para cada consulta.            | Processo automatizado para recuperação e geração.      |
| **Controlo**            | Oferece mais controlo sobre o processo de recuperação.   | Simplifica e automatiza a recuperação e geração.       |
| **Flexibilidade**        | Permite prompts personalizados baseados em necessidades.| Mais eficiente para implementações em larga escala.    |
| **Complexidade**         | Requer elaboração e ajuste de prompts.                   | Mais fácil de integrar na arquitetura de um agente IA. |

### Exemplos Práticos

**Exemplo de Técnica de Prompting:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Exemplo de Ferramenta:**

```python
class Travel_Agent:
    def __init__(self):
        self.rag_tool = RAGTool()

    def get_museums_in_paris(self):
        user_input = "I want to visit museums in Paris."
        response = self.rag_tool.retrieve_and_generate(user_input)
        return response

travel_agent = Travel_Agent()
museums = travel_agent.get_museums_in_paris()
print("Top Museums in Paris:", museums)
```

### Avaliação de Relevância

Avaliar a relevância é um aspeto crucial no desempenho de agentes de IA. Garante que a informação recuperada e gerada pelo agente é adequada, precisa e útil para o utilizador. Vamos explorar como avaliar a relevância em agentes de IA, incluindo exemplos práticos e técnicas.

#### Conceitos-Chave na Avaliação de Relevância

1. **Consciência do Contexto**:
   - O agente deve compreender o contexto da consulta do utilizador para recuperar e gerar informação relevante.
   - Exemplo: Se um utilizador pede "melhores restaurantes em Paris," o agente deve considerar as preferências do utilizador, como tipo de cozinha e orçamento.

2. **Precisão**:
   - A informação fornecida pelo agente deve ser factual e atualizada.
   - Exemplo: Recomendar restaurantes atualmente abertos com boas críticas, em vez de opções antigas ou encerradas.

3. **Intenção do Utilizador**:
   - O agente deve inferir a intenção do utilizador por trás da consulta para fornecer a informação mais relevante.
   - Exemplo: Se um utilizador pede "hotéis económicos," o agente deve priorizar opções acessíveis.

4. **Ciclo de Feedback**:
   - Recolher e analisar continuamente feedback dos utilizadores ajuda o agente a aprimorar o seu processo de avaliação de relevância.
   - Exemplo: Incorporar avaliações e feedback dos utilizadores sobre recomendações anteriores para melhorar respostas futuras.

#### Técnicas Práticas para Avaliação de Relevância

1. **Pontuação de Relevância**:
   - Atribuir uma pontuação de relevância a cada item recuperado com base no seu grau de correspondência à consulta e preferências do utilizador.
   - Exemplo:

     ```python
     def relevance_score(item, query):
         score = 0
         if item['category'] in query['interests']:
             score += 1
         if item['price'] <= query['budget']:
             score += 1
         if item['location'] == query['destination']:
             score += 1
         return score
     ```

2. **Filtragem e Ranking**:
   - Filtrar itens irrelevantes e classificar os restantes com base nas pontuações de relevância.
   - Exemplo:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Retorna os 10 itens mais relevantes
     ```

3. **Processamento de Linguagem Natural (PLN)**:
   - Usar técnicas de PLN para compreender a consulta do utilizador e recuperar informação relevante.
   - Exemplo:

     ```python
     def process_query(query):
         # Use PNL para extrair informações chave da consulta do utilizador
         processed_query = nlp(query)
         return processed_query
     ```

4. **Integração de Feedback do Utilizador**:
   - Recolher feedback do utilizador sobre as recomendações fornecidas e usá-lo para ajustar avaliações futuras de relevância.
   - Exemplo:

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### Exemplo: Avaliação da Relevância no Agente de Viagens

Aqui está um exemplo prático de como o Agente de Viagens pode avaliar a relevância das recomendações de viagem:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        ranked_hotels = self.filter_and_rank(hotels, self.user_preferences)
        itinerary = create_itinerary(flights, ranked_hotels, attractions)
        return itinerary

    def filter_and_rank(self, items, query):
        ranked_items = sorted(items, key=lambda item: self.relevance_score(item, query), reverse=True)
        return ranked_items[:10]  # Retornar os 10 itens mais relevantes

    def relevance_score(self, item, query):
        score = 0
        if item['category'] in query['interests']:
            score += 1
        if item['price'] <= query['budget']:
            score += 1
        if item['location'] == query['destination']:
            score += 1
        return score

    def adjust_based_on_feedback(self, feedback, items):
        for item in items:
            if item['name'] in feedback['liked']:
                item['relevance'] += 1
            if item['name'] in feedback['disliked']:
                item['relevance'] -= 1
        return items

# Exemplo de utilização
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```

### Pesquisa com Intenção

Pesquisar com intenção envolve compreender e interpretar o propósito ou objetivo subjacente a uma consulta do utilizador para recuperar e gerar a informação mais relevante e útil. Esta abordagem vai além de simplesmente corresponder palavras-chave e foca-se em perceber as reais necessidades e contexto do utilizador.

#### Conceitos-Chave em Pesquisa com Intenção

1. **Compreensão da Intenção do Utilizador**:
   - A intenção do utilizador pode ser categorizada em três tipos principais: informacional, navegacional e transacional.
     - **Intenção Informacional**: O utilizador procura informação sobre um tópico (ex.: "Quais são os melhores museus em Paris?").
     - **Intenção Navegacional**: O utilizador quer navegar para um website ou página específica (ex.: "Site oficial do Museu do Louvre").
     - **Intenção Transacional**: O utilizador pretende realizar uma transação, como reservar um voo ou fazer uma compra (ex.: "Reservar voo para Paris").

2. **Consciência do Contexto**:
   - Analisar o contexto da consulta do utilizador ajuda a identificar com precisão a sua intenção. Isto inclui considerar interações anteriores, preferências do utilizador e detalhes específicos da consulta atual.

3. **Processamento de Linguagem Natural (PLN)**:
   - Técnicas de PLN são usadas para compreender e interpretar as consultas em linguagem natural fornecidas pelos utilizadores. Inclui tarefas como reconhecimento de entidades, análise de sentimento e parsing de consultas.

4. **Personalização**:
   - Personalizar os resultados da pesquisa com base no histórico, preferências e feedback do utilizador melhora a relevância da informação recuperada.

#### Exemplo Prático: Pesquisa com Intenção no Agente de Viagens

Vamos usar o Agente de Viagens como exemplo para ver como a pesquisa com intenção pode ser implementada.

1. **Recolher Preferências do Utilizador**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Compreender a Intenção do Utilizador**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Consciência do Contexto**


   ```python
   def analyze_context(query, user_history):
       # Combine a consulta atual com o histórico do utilizador para entender o contexto
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Pesquisar e Personalizar Resultados**

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # Exemplo de lógica de pesquisa para intenção informativa
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Exemplo de lógica de pesquisa para intenção de navegação
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Exemplo de lógica de pesquisa para intenção transacional
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Exemplo de lógica de personalização
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Retornar os 10 melhores resultados personalizados
   ```

5. **Exemplo de Utilização**

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. Gerar Código como uma Ferramenta

Agentes geradores de código usam modelos de IA para escrever e executar código, resolvendo problemas complexos e automatizando tarefas.

### Agentes Geradores de Código

Agentes geradores de código usam modelos generativos de IA para escrever e executar código. Estes agentes podem resolver problemas complexos, automatizar tarefas e fornecer insights valiosos ao gerar e executar código em várias linguagens de programação.

#### Aplicações Práticas

1. **Geração Automática de Código**: Gerar trechos de código para tarefas específicas, como análise de dados, web scraping ou aprendizagem automática.
2. **SQL como RAG**: Usar consultas SQL para recuperar e manipular dados em bases de dados.
3. **Resolução de Problemas**: Criar e executar código para resolver problemas específicos, como otimizar algoritmos ou analisar dados.

#### Exemplo: Agente Gerador de Código para Análise de Dados

Imagine que está a desenhar um agente gerador de código. Eis como pode funcionar:

1. **Tarefa**: Analisar um conjunto de dados para identificar tendências e padrões.
2. **Passos**:
   - Carregar o conjunto de dados numa ferramenta de análise de dados.
   - Gerar consultas SQL para filtrar e agregar os dados.
   - Executar as consultas e recuperar os resultados.
   - Usar os resultados para gerar visualizações e insights.
3. **Recursos Necessários**: Acesso ao conjunto de dados, ferramentas de análise de dados e capacidades SQL.
4. **Experiência**: Usar resultados de análises anteriores para melhorar a precisão e relevância de análises futuras.

### Exemplo: Agente Gerador de Código para Agente de Viagens

Neste exemplo, vamos desenhar um agente gerador de código, Agente de Viagens, para ajudar utilizadores a planear as suas viagens gerando e executando código. Este agente pode gerir tarefas como obter opções de viagens, filtrar resultados e compilar um itinerário usando IA generativa.

#### Visão Geral do Agente Gerador de Código

1. **Recolha de Preferências do Utilizador**: Recolhe inputs do utilizador como destino, datas da viagem, orçamento e interesses.
2. **Gerar Código para Obter Dados**: Gera trechos de código para recuperar dados sobre voos, hotéis e atrações.
3. **Executar Código Gerado**: Executa o código gerado para obter informações em tempo real.
4. **Gerar Itinerário**: Compila os dados obtidos num plano de viagem personalizado.
5. **Ajustar com Base no Feedback**: Recebe feedback do utilizador e regenera código se necessário para refinar os resultados.

#### Implementação Passo a Passo

1. **Recolha de Preferências do Utilizador**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Gerar Código para Obter Dados**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Exemplo: Gerar código para procurar voos com base nas preferências do utilizador
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Exemplo: Gerar código para procurar hotéis
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Executar Código Gerado**

   ```python
   def execute_code(code):
       # Execute o código gerado usando exec
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. **Gerar Itinerário**

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. **Ajustar com Base no Feedback**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Ajustar as preferências com base no feedback do utilizador
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerar e executar o código com as preferências atualizadas
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Aproveitar a perceção ambiental e o raciocínio

Basear-se no esquema da tabela pode, de facto, melhorar o processo de geração de consultas ao aproveitar a perceção ambiental e o raciocínio.

Eis um exemplo de como isso pode ser feito:

1. **Compreender o Esquema**: O sistema irá compreender o esquema da tabela e usar esta informação para fundamentar a geração de consultas.
2. **Ajustar com Base no Feedback**: O sistema ajusta as preferências do utilizador com base no feedback e raciocina sobre quais os campos no esquema que necessitam ser atualizados.
3. **Gerar e Executar Consultas**: O sistema gera e executa consultas para obter dados atualizados de voos e hotéis, baseando-se nas novas preferências.

Aqui está um exemplo atualizado em Python que incorpora estes conceitos:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Ajustar preferências com base no feedback do utilizador
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Raciocínio baseado no esquema para ajustar outras preferências relacionadas
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Lógica personalizada para ajustar preferências com base no esquema e no feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Gerar código para obter dados de voos com base nas preferências atualizadas
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Gerar código para obter dados de hotéis com base nas preferências atualizadas
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simular a execução do código e retornar dados simulados
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Gerar itinerário com base em voos, hotéis e atrações
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Exemplo de esquema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Exemplo de utilização
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Regenerar e executar código com preferências atualizadas
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Explicação - Reserva com Base no Feedback

1. **Consciência do Esquema**: O dicionário `schema` define como as preferências devem ser ajustadas com base no feedback. Inclui campos como `favorites` e `avoid`, com ajustes correspondentes.
2. **Ajustar Preferências (método `adjust_based_on_feedback`)**: Este método ajusta as preferências com base no feedback do utilizador e no esquema.
3. **Ajustes Baseados no Ambiente (método `adjust_based_on_environment`)**: Este método personaliza os ajustes com base no esquema e no feedback.
4. **Gerar e Executar Consultas**: O sistema gera código para obter dados atualizados de voos e hotéis com base nas preferências ajustadas e simula a execução dessas consultas.
5. **Gerar Itinerário**: O sistema cria um itinerário atualizado com base nos novos dados de voos, hotéis e atrações.

Tornando o sistema consciente do ambiente e raciocinando com base no esquema, ele pode gerar consultas mais precisas e relevantes, conduzindo a melhores recomendações de viagens e uma experiência mais personalizada para o utilizador.

### Usar SQL como uma Técnica de Geração Aumentada por Recuperação (RAG)

SQL (Structured Query Language) é uma ferramenta poderosa para interagir com bases de dados. Quando usada como parte de uma abordagem de Geração Aumentada por Recuperação (RAG), SQL pode recuperar dados relevantes das bases de dados para informar e gerar respostas ou ações em agentes de IA. Vamos explorar como SQL pode ser usada como técnica RAG no contexto do Agente de Viagens.

#### Conceitos-Chave

1. **Interação com a Base de Dados**:
   - SQL é usada para consultar bases de dados, recuperar informações relevantes e manipular dados.
   - Exemplo: Obter detalhes de voos, informações de hotéis e atrações de uma base de dados de viagens.

2. **Integração com RAG**:
   - Consultas SQL são geradas com base no input e preferências do utilizador.
   - Os dados obtidos são então usados para gerar recomendações ou ações personalizadas.

3. **Geração Dinâmica de Consultas**:
   - O agente IA gera consultas SQL dinâmicas baseando-se no contexto e nas necessidades do utilizador.
   - Exemplo: Personalizar consultas SQL para filtrar resultados baseado no orçamento, datas e interesses.

#### Aplicações

- **Geração Automática de Código**: Gerar trechos de código para tarefas específicas.
- **SQL como RAG**: Usar consultas SQL para manipular dados.
- **Resolução de Problemas**: Criar e executar código para resolver problemas.

**Exemplo**:
Um agente de análise de dados:

1. **Tarefa**: Analisar um conjunto de dados para encontrar tendências.
2. **Passos**:
   - Carregar o conjunto de dados.
   - Gerar consultas SQL para filtrar os dados.
   - Executar consultas e obter resultados.
   - Gerar visualizações e insights.
3. **Recursos**: Acesso ao conjunto de dados, capacidades SQL.
4. **Experiência**: Usar resultados anteriores para melhorar análises futuras.

#### Exemplo Prático: Usando SQL no Agente de Viagens

1. **Recolha de Preferências do Utilizador**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Gerar Consultas SQL**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Executar Consultas SQL**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. **Gerar Recomendações**

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### Exemplo de Consultas SQL

1. **Consulta de Voos**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Consulta de Hotéis**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Consulta de Atrações**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Aproveitando SQL como parte da técnica de Geração Aumentada por Recuperação (RAG), agentes de IA como o Agente de Viagens podem recuperar e usar dados relevantes dinamicamente para fornecer recomendações precisas e personalizadas.

### Exemplo de Metacognição

Para demonstrar uma implementação de metacognição, vamos criar um agente simples que *reflete sobre o seu processo de tomada de decisão* enquanto resolve um problema. Neste exemplo, vamos construir um sistema onde um agente tenta otimizar a escolha de um hotel, mas depois avalia o seu próprio raciocínio e ajusta a sua estratégia quando comete erros ou faz escolhas subótimas.

Vamos simular isto usando um exemplo básico onde o agente seleciona hotéis com base numa combinação de preço e qualidade, mas irá "refletir" sobre as suas decisões e ajustar conforme necessário.

#### Como isto ilustra a metacognição:

1. **Decisão Inicial**: O agente escolhe o hotel mais barato, sem perceber o impacto da qualidade.
2. **Reflexão e Avaliação**: Após a escolha inicial, o agente verifica se o hotel foi uma escolha "má" usando o feedback do utilizador. Se descobrir que a qualidade do hotel foi demasiado baixa, reflete sobre o seu raciocínio.
3. **Ajustar Estratégia**: O agente ajusta a sua estratégia com base na reflexão, mudando de "mais barato" para "melhor qualidade", assim melhorando o seu processo de decisão em iterações futuras.

Aqui está um exemplo:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Armazena os hotéis escolhidos anteriormente
        self.corrected_choices = []  # Armazena as escolhas corrigidas
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Estratégias disponíveis

    def recommend_hotel(self, hotels, strategy):
        """
        Recommend a hotel based on the chosen strategy.
        The strategy can either be 'cheapest' or 'highest_quality'.
        """
        if strategy == 'cheapest':
            recommended = min(hotels, key=lambda x: x['price'])
        elif strategy == 'highest_quality':
            recommended = max(hotels, key=lambda x: x['quality'])
        else:
            recommended = None
        self.previous_choices.append((strategy, recommended))
        return recommended

    def reflect_on_choice(self):
        """
        Reflect on the last choice made and decide if the agent should adjust its strategy.
        The agent considers if the previous choice led to a poor outcome.
        """
        if not self.previous_choices:
            return "No choices made yet."

        last_choice_strategy, last_choice = self.previous_choices[-1]
        # Vamos supor que temos algum feedback do utilizador que nos diz se a última escolha foi boa ou não
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Ajustar a estratégia se a escolha anterior foi insatisfatória
            new_strategy = 'highest_quality' if last_choice_strategy == 'cheapest' else 'cheapest'
            self.corrected_choices.append((new_strategy, last_choice))
            return f"Reflecting on choice. Adjusting strategy to {new_strategy}."
        else:
            return "The choice was good. No need to adjust."

    def get_user_feedback(self, hotel):
        """
        Simulate user feedback based on hotel attributes.
        For simplicity, assume if the hotel is too cheap, the feedback is "bad".
        If the hotel has quality less than 7, feedback is "bad".
        """
        if hotel['price'] < 100 or hotel['quality'] < 7:
            return "bad"
        return "good"

# Simular uma lista de hotéis (preço e qualidade)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Criar um agente
agent = HotelRecommendationAgent()

# Passo 1: O agente recomenda um hotel usando a estratégia "mais barato"
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Passo 2: O agente reflete sobre a escolha e ajusta a estratégia se necessário
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Passo 3: O agente recomenda novamente, desta vez usando a estratégia ajustada
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Capacidades de Metacognição do Agente

O essencial aqui é a capacidade do agente de:
- Avaliar as suas escolhas anteriores e o processo de tomada de decisão.
- Ajustar a sua estratégia com base nessa reflexão, isto é, metacognição em ação.

Esta é uma forma simples de metacognição onde o sistema é capaz de ajustar o seu processo de raciocínio com base no feedback interno.

### Conclusão

A metacognição é uma ferramenta poderosa que pode melhorar significativamente as capacidades dos agentes IA. Ao incorporar processos metacognitivos, pode desenhar agentes mais inteligentes, adaptáveis e eficientes. Use os recursos adicionais para explorar mais o fascinante mundo da metacognição em agentes IA.

### Tem mais perguntas sobre o Padrão de Design Metacognição?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conhecer outros aprendizes, participar em horas de atendimento e obter respostas às suas perguntas sobre Agentes IA.

## Aula Anterior

[Padrão de Design Multiagente](../08-multi-agent/README.md)

## Próxima Aula

[Agentes IA em Produção](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->