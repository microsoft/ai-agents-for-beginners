[![Padrão de Design de Planejamento](../../../translated_images/pt-BR/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

# Planejamento de Design

## Introdução

Esta lição cobrirá

* Definir um objetivo geral claro e dividir uma tarefa complexa em tarefas gerenciáveis.
* Aproveitar saída estruturada para respostas mais confiáveis e legíveis por máquina.
* Aplicar uma abordagem orientada a eventos para lidar com tarefas dinâmicas e entradas inesperadas.

## Objetivos de Aprendizagem

Após concluir esta lição, você terá uma compreensão sobre:

* Identificar e definir um objetivo geral para um agente de IA, garantindo que ele saiba claramente o que precisa ser alcançado.
* Decompor uma tarefa complexa em subtarefas gerenciáveis e organizá-las em uma sequência lógica.
* Equipar agentes com as ferramentas certas (por exemplo, ferramentas de busca ou de análise de dados), decidir quando e como utilizá-las, e lidar com situações inesperadas que surgirem.
* Avaliar os resultados das subtarefas, medir o desempenho e iterar as ações para melhorar a saída final.

## Definindo o Objetivo Geral e Dividindo uma Tarefa

![Definindo Objetivos e Tarefas](../../../translated_images/pt-BR/defining-goals-tasks.d70439e19e37c47a.webp)

A maioria das tarefas do mundo real é complexa demais para ser resolvida em um único passo. Um agente de IA precisa de um objetivo conciso para orientar seu planejamento e ações. Por exemplo, considere o objetivo:

    "Gerar um roteiro de viagem de 3 dias."

Embora seja simples de afirmar, ainda precisa de refinamento. Quanto mais claro o objetivo, melhor o agente (e quaisquer colaboradores humanos) podem focar em alcançar o resultado certo, como criar um roteiro abrangente com opções de voos, recomendações de hotéis e sugestões de atividades.

### Decomposição de Tarefa

Tarefas grandes ou complexas tornam-se mais gerenciáveis quando divididas em subtarefas menores, orientadas por objetivos.
Para o exemplo do roteiro de viagem, você poderia decompor o objetivo em:

* Reserva de Voo
* Reserva de Hotel
* Aluguel de Carro
* Personalização

Cada subtarefa pode então ser tratada por agentes ou processos dedicados. Um agente pode se especializar em buscar as melhores ofertas de voos, outro foca nas reservas de hotéis, e assim por diante. Um agente coordenador ou “downstream” pode compilar esses resultados em um único roteiro coeso para o usuário final.

Essa abordagem modular também permite melhorias incrementais. Por exemplo, você poderia adicionar agentes especializados para Recomendações de Alimentação ou Sugestões de Atividades Locais e aprimorar o roteiro ao longo do tempo.

### Saída Estruturada

Modelos de Linguagem de Grande Porte (LLMs) podem gerar saída estruturada (por exemplo, JSON) que é mais fácil para agentes ou serviços downstream analisarem e processarem. Isso é especialmente útil em um contexto multiagente, onde podemos agir nessas tarefas após receber a saída do planejamento.

O trecho de código Python a seguir demonstra um agente de planejamento simples decompondo um objetivo em subtarefas e gerando um plano estruturado:

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

# Definir a mensagem do usuário
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

### Agente de Planejamento com Orquestração Multiagente

Neste exemplo, um Agente Roteador Semântico recebe uma solicitação do usuário (por exemplo, "Preciso de um plano de hotel para minha viagem.").

O planejador então:

* Recebe o Plano de Hotel: O planejador pega a mensagem do usuário e, baseado em um prompt do sistema (incluindo detalhes dos agentes disponíveis), gera um plano de viagem estruturado.
* Lista os Agentes e Suas Ferramentas: O registro de agentes contém uma lista de agentes (por exemplo, para voo, hotel, aluguel de carro e atividades) junto com as funções ou ferramentas que oferecem.
* Roteia o Plano para os Agentes Respectivos: Dependendo do número de subtarefas, o planejador envia a mensagem diretamente para um agente dedicado (para cenários de tarefa única) ou coordena via um gerente de chat em grupo para colaboração multiagente.
* Resume o Resultado: Finalmente, o planejador resume o plano gerado para clareza.
O código Python a seguir ilustra essas etapas:

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

# Definir a mensagem do usuário

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

O que segue é a saída do código anterior e você pode usar essa saída estruturada para encaminhar ao `assigned_agent` e resumir o plano de viagem para o usuário final.

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

### Planejamento Iterativo

Algumas tarefas requerem um vai e vem ou replanejamento, onde o resultado de uma subtarefa influencia a próxima. Por exemplo, se o agente descobrir um formato de dado inesperado ao reservar voos, pode ser necessário adaptar sua estratégia antes de avançar para as reservas de hotel.

Além disso, o feedback do usuário (por exemplo, um humano decidindo que prefere um voo mais cedo) pode disparar um replanejamento parcial. Essa abordagem iterativa e dinâmica garante que a solução final esteja alinhada com as restrições do mundo real e as preferências do usuário em evolução.

exemplo de código

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. mesmo que o código anterior e repassa o histórico do usuário, plano atual

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
# .. replanejar e enviar as tarefas para os agentes respectivos
```

Para um planejamento mais abrangente, confira o Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> sobre resolução de tarefas complexas.

## Resumo

Neste artigo, vimos um exemplo de como podemos criar um planejador que pode selecionar dinamicamente os agentes disponíveis definidos. A saída do Planejador decompõe as tarefas e atribui os agentes para que possam ser executados. Presume-se que os agentes tenham acesso às funções/ferramentas necessárias para realizar a tarefa. Além dos agentes, você pode incluir outros padrões como reflexão, sumarizador e chat round robin para personalizar ainda mais.

## Recursos Adicionais

Magentic One - Um sistema multiagente generalista para resolver tarefas complexas que alcançou resultados impressionantes em vários benchmarks agentísticos desafiadores. Referência: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. Nesta implementação, o orquestrador cria planos específicos para as tarefas e delega essas tarefas aos agentes disponíveis. Além do planejamento, o orquestrador também emprega um mecanismo de monitoramento para acompanhar o progresso da tarefa e replaneja conforme necessário.

### Quer Mais Perguntas sobre o Padrão de Design de Planejamento?

Junte-se ao [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para encontrar outros aprendizes, participar de horários de atendimento e obter respostas para suas perguntas sobre Agentes de IA.

## Lição Anterior

[Construindo Agentes de IA Confiáveis](../06-building-trustworthy-agents/README.md)

## Próxima Lição

[Padrão de Design Multiagente](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->