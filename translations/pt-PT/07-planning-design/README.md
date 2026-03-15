[![Padrão de Planeamento](../../../translated_images/pt-PT/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Clique na imagem acima para ver o vídeo desta lição)_

# Padrão de Planeamento

## Introdução

Esta lição irá abordar

* Definir um objetivo geral claro e decompor uma tarefa complexa em tarefas geríveis.
* Aproveitar saídas estruturadas para respostas mais fiáveis e legíveis por máquina.
* Aplicar uma abordagem orientada a eventos para lidar com tarefas dinâmicas e entradas inesperadas.

## Objetivos de Aprendizagem

Após completar esta lição, irá compreender:

* Identificar e definir um objetivo geral para um agente de IA, garantindo que sabe claramente o que precisa ser alcançado.
* Decompor uma tarefa complexa em subtarefas geríveis e organizá-las numa sequência lógica.
* Equipar agentes com as ferramentas certas (por exemplo, ferramentas de pesquisa ou de análise de dados), decidir quando e como são utilizadas e tratar situações inesperadas que surjam.
* Avaliar os resultados das subtarefas, medir desempenho e iterar ações para melhorar o resultado final.

## Definir o Objetivo Geral e Decompor uma Tarefa

![Definir Objetivos e Tarefas](../../../translated_images/pt-PT/defining-goals-tasks.d70439e19e37c47a.webp)

A maioria das tarefas do mundo real é demasiado complexa para ser tratada num único passo. Um agente de IA necessita de um objetivo conciso para orientar o seu planeamento e ações. Por exemplo, considere o objetivo:

    "Gerar um itinerário de viagem de 3 dias."

Embora seja simples de enunciar, ainda necessita de refinamento. Quanto mais claro o objetivo, melhor o agente (e quaisquer colaboradores humanos) poderão concentrar-se em alcançar o resultado certo, como criar um itinerário abrangente com opções de voos, recomendações de hotéis e sugestões de atividades.

### Decomposição de Tarefas

Tarefas grandes ou intrincadas tornam-se mais geríveis quando divididas em subtarefas mais pequenas e orientadas por objetivos.
Para o exemplo do itinerário de viagem, poderia decompor o objetivo em:

* Reserva de Voos
* Reserva de Hotel
* Aluguer de Carro
* Personalização

Cada subtarefa pode então ser tratada por agentes ou processos dedicados. Um agente pode especializar-se em procurar as melhores ofertas de voos, outro concentra-se nas reservas de hotel, e assim por diante. Um agente coordenador ou “downstream” pode então compilar estes resultados num único itinerário coerente para o utilizador final.

Esta abordagem modular também permite melhorias incrementais. Por exemplo, poderia adicionar agentes especializados para Recomendações Gastronómicas ou Sugestões de Atividades Locais e refinar o itinerário ao longo do tempo.

### Saída estruturada

Modelos de Linguagem de Grande Escala (LLMs) podem gerar saídas estruturadas (por exemplo, JSON) que são mais fáceis de serem analisadas e processadas por agentes ou serviços a jusante. Isto é especialmente útil num contexto multi-agente, onde podemos executar estas tarefas após a receção da saída de planeamento.

O seguinte fragmento em Python demonstra um agente de planeamento simples a decompor um objetivo em subtarefas e a gerar um plano estruturado:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.azure import AzureAIProjectAgentProvider
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

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Defina a mensagem do utilizador
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

Neste exemplo, um Agente Encaminhador Semântico recebe um pedido do utilizador (por exemplo, "Preciso de um plano de hotel para a minha viagem.").

O planeador depois:

* Recebe o Plano de Hotel: O planeador pega na mensagem do utilizador e, com base num prompt do sistema (incluindo detalhes dos agentes disponíveis), gera um plano de viagem estruturado.
* Lista Agentes e As Suas Ferramentas: o registo de agentes contém uma lista de agentes (por exemplo, para voos, hotéis, aluguer de carros e atividades) juntamente com as funções ou ferramentas que oferecem.
* Encaminha o Plano para os Agentes Correspondentes: Dependendo do número de subtarefas, o planeador ou envia a mensagem diretamente para um agente dedicado (para cenários de tarefa única) ou coordena via um gestor de chat de grupo para colaboração multi-agente.
* Resume o Resultado: Finalmente, o planeador resume o plano gerado para maior clareza.
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

# Modelo de Subtarefa de Viagem

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

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Criar o cliente

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

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

# Imprimir o conteúdo da resposta após o carregar como JSON

pprint(json.loads(response_content))
```

O que se segue é a saída do código anterior e pode então usar esta saída estruturada para encaminhar para `assigned_agent` e resumir o plano de viagem ao utilizador final.

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

Um notebook de exemplo com o código anterior está disponível [aqui](07-python-agent-framework.ipynb).

### Planeamento Iterativo

Algumas tarefas requerem um processo de ida e volta ou um replaneamento, onde o resultado de uma subtarefa influencia a seguinte. Por exemplo, se o agente descobrir um formato de dados inesperado ao reservar voos, pode ser necessário adaptar a sua estratégia antes de prosseguir para as reservas de hotel.

Adicionalmente, o feedback do utilizador (por exemplo, um humano decidir que prefere um voo mais cedo) pode desencadear um replaneamento parcial. Esta abordagem dinâmica e iterativa garante que a solução final se alinha com as restrições do mundo real e com as preferências do utilizador em evolução.

exemplo de código

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. igual ao código anterior e transmitir o histórico do utilizador e o plano atual

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
# .. replanear e enviar as tarefas aos respectivos agentes
```

Para um planeamento mais abrangente, consulte o artigo do Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Publicação no blog</a> sobre a resolução de tarefas complexas.

## Resumo

Neste artigo analisámos um exemplo de como podemos criar um planeador que consegue selecionar dinamicamente os agentes disponíveis definidos. A saída do Planeador decompoe as tarefas e atribui os agentes para que estas possam ser executadas. Presume-se que os agentes têm acesso às funções/ferramentas necessárias para executar a tarefa. Para além dos agentes, pode incluir outros padrões como reflexão, resumidor e chat round robin para personalizar ainda mais.

## Recursos Adicionais

Magentic One - A Generalist multi-agent system for solving complex tasks and has achieved impressive results on multiple challenging agentic benchmarks. Referência: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. Nesta implementação o orquestrador cria planos específicos por tarefa e delega essas tarefas aos agentes disponíveis. Para além do planeamento, o orquestrador também emprega um mecanismo de acompanhamento para monitorizar o progresso da tarefa e replanear conforme necessário.

### Tem mais perguntas sobre o Padrão de Planeamento?

Junte-se ao [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para conhecer outros aprendizes, participar em horas de atendimento e esclarecer as suas questões sobre Agentes de IA.

## Lição Anterior

[Construir Agentes de IA Confiáveis](../06-building-trustworthy-agents/README.md)

## Próxima Lição

[Padrão Multi-Agente](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Aviso legal:
Este documento foi traduzido através do serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original, na sua língua nativa, deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se uma tradução profissional por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erróneas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->