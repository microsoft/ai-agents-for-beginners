[![Planning Design Pattern](../../../translated_images/pt-PT/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Clique na imagem acima para assistir ao vídeo desta aula)_

# Planeamento de Design

## Introdução

Esta aula irá abordar

* Definir um objetivo geral claro e decompor uma tarefa complexa em tarefas geríveis.
* Aproveitar a saída estruturada para respostas mais fiáveis e legíveis por máquina.
* Aplicar uma abordagem orientada a eventos para lidar com tarefas dinâmicas e entradas inesperadas.

## Objetivos de Aprendizagem

Após concluir esta aula, irá compreender:

* Identificar e definir um objetivo global para um agente de IA, garantindo que sabe claramente o que precisa ser alcançado.
* Decompor uma tarefa complexa em subtarefas geríveis e organizá-las numa sequência lógica.
* Equipar agentes com as ferramentas certas (por ex., ferramentas de pesquisa ou análise de dados), decidir quando e como são usadas, e lidar com situações inesperadas que surgem.
* Avaliar os resultados das subtarefas, medir o desempenho e iterar nas ações para melhorar o resultado final.

## Definir o Objetivo Geral e Decompor uma Tarefa

![Defining Goals and Tasks](../../../translated_images/pt-PT/defining-goals-tasks.d70439e19e37c47a.webp)

A maioria das tarefas do mundo real é demasiado complexa para ser abordada num único passo. Um agente de IA necessita de um objetivo conciso para guiar o seu planeamento e ações. Por exemplo, considere o objetivo:

    "Gerar um itinerário de viagem de 3 dias."

Embora seja simples de enunciar, ainda precisa de refinamento. Quanto mais claro for o objetivo, melhor o agente (e quaisquer colaboradores humanos) podem focar-se em alcançar o resultado correto, como criar um itinerário abrangente com opções de voos, recomendações de hotéis e sugestões de atividades.

### Decomposição de Tarefas

Tarefas grandes ou complexas tornam-se mais geríveis quando divididas em subtarefas menores, orientadas por objetivos.
Para o exemplo do itinerário de viagem, pode decompor o objetivo em:

* Reserva de Voos
* Reserva de Hotéis
* Aluguer de Carros
* Personalização

Cada subtarefa pode depois ser tratada por agentes ou processos dedicados. Um agente pode especializar-se em procurar as melhores ofertas de voos, outro foca-se nas reservas de hotéis, e assim sucessivamente. Um agente coordenador ou “a jusante” pode então compilar estes resultados num itinerário coeso para o utilizador final.

Esta abordagem modular permite igualmente melhorias incrementais. Por exemplo, pode adicionar agentes especializados para Recomendações Alimentares ou Sugestões de Atividades Locais e refinar o itinerário ao longo do tempo.

### Saída estruturada

Os Modelos de Linguagem Grande (LLMs) podem gerar uma saída estruturada (ex. JSON) que é mais fácil para agentes ou serviços subsequentes analisarem e processarem. Isso é especialmente útil num contexto de multi-agente, onde podemos executar estas tarefas após receber a saída do planeamento.

O seguinte trecho de Python demonstra um agente de planeamento simples a decompor um objetivo em subtarefas e gerar um plano estruturado:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Modelo de Subtarefa de Viagem
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # queremos atribuir a tarefa ao agente

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Definir a mensagem do utilizador
system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Provide your response in JSON format with the following structure:
{'main_task': 'Plan a family trip from Singapore to Melbourne.',
 'subtasks': [{'assigned_agent': 'flight_booking',
               'task_details': 'Book round-trip flights from Singapore to '
                               'Melbourne.'}
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text
pprint(json.loads(response_content))
```

### Agente de Planeamento com Orquestração Multi-Agente

Neste exemplo, um Agente Roteador Semântico recebe um pedido do utilizador (ex., "Preciso de um plano de hotel para a minha viagem.").

O planeador então:

* Recebe o Plano de Hotel: O planeador pega na mensagem do utilizador e, com base num prompt de sistema (incluindo detalhes dos agentes disponíveis), gera um plano de viagem estruturado.
* Lista os Agentes e as Suas Ferramentas: O registo de agentes contém uma lista de agentes (ex., para voos, hotéis, aluguer de carros, e atividades) juntamente com as funções ou ferramentas que oferecem.
* Encaminha o Plano para os Agentes Respetivos: Dependendo do número de subtarefas, o planeador envia a mensagem diretamente a um agente dedicado (para cenários de tarefa única) ou coordena via um gestor de chat de grupo para colaboração multi-agente.
* Resume o Resultado: Finalmente, o planeador resume o plano gerado para clarificação.
O seguinte exemplo de código Python ilustra estes passos:

```python

from pydantic import BaseModel

from enum import Enum
from typing import List, Optional, Union

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Modelo de SubTarefa de Viagem

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # queremos atribuir a tarefa ao agente

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Criar o cliente

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# Definir a mensagem do utilizador

system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text

# Imprimir o conteúdo da resposta após carregá-lo como JSON

pprint(json.loads(response_content))
```

O que se segue é a saída do código anterior e pode então utilizar esta saída estruturada para encaminhar para `assigned_agent` e resumir o plano de viagem para o utilizador final.

```json
{
    "is_greeting": "False",
    "main_task": "Plan a family trip from Singapore to Melbourne.",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "Book round-trip flights from Singapore to Melbourne."
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "Find family-friendly hotels in Melbourne."
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "Arrange a car rental suitable for a family of four in Melbourne."
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "List family-friendly activities in Melbourne."
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "Provide information about Melbourne as a travel destination."
        }
    ]
}
```

Um notebook de exemplo com o código anterior está disponível [aqui](./code_samples/07-python-agent-framework.ipynb).

### Planeamento Iterativo

Algumas tarefas requerem um vai-e-volta ou replaneamento, onde o resultado de uma subtarefa influencia a seguinte. Por exemplo, se o agente descobrir um formato de dados inesperado ao reservar voos, poderá precisar adaptar a sua estratégia antes de avançar para reservas de hotéis.

Além disso, o feedback do utilizador (ex. um humano decidir que prefere um voo mais cedo) pode desencadear um replaneamento parcial. Esta abordagem dinâmica e iterativa assegura que a solução final está alinhada com as restrições do mundo real e preferências do utilizador em evolução.

ex. código de exemplo

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. igual ao código anterior e passar o histórico do utilizador, plano atual

system_prompt = """You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(
    input=user_message,
    instructions=system_prompt,
    context=f"Previous travel plan - {TravelPlan}",
)
# .. replanejar e enviar as tarefas aos respetivos agentes
```

Para um planeamento mais abrangente consulte o Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> para resolução de tarefas complexas.

## Sumário

Neste artigo vimos um exemplo de como criar um planeador capaz de seleccionar dinamicamente os agentes disponíveis definidos. A saída do Planeador decompõe as tarefas e atribui os agentes para que possam ser executadas. Assume-se que os agentes têm acesso às funções/ferramentas necessárias para realizar a tarefa. Para além dos agentes pode incluir outros padrões como reflexão, sumarizador e chat round robin para personalizar ainda mais.

## Recursos Adicionais

Magnetic One - Um sistema multi-agente generalista para resolver tarefas complexas que obteve resultados impressionantes em múltiplos benchmarks agentic desafiantes. Referência: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. Nesta implementação o orquestrador cria planos específicos para tarefas e delega essas tarefas aos agentes disponíveis. Para além do planeamento, o orquestrador também utiliza um mecanismo de acompanhamento para monitorizar o progresso da tarefa e replaneia conforme necessário.

### Tem Mais Perguntas sobre o Padrão de Design de Planeamento?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conhecer outros aprendizes, participar em horas de atendimento e esclarecer dúvidas sobre Agentes de IA.

## Aula Anterior

[Construir Agentes de IA Confiáveis](../06-building-trustworthy-agents/README.md)

## Próxima Aula

[Padrão de Design Multi-Agente](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->