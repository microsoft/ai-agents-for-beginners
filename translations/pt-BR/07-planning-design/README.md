[![Padrão de Design de Planejamento](../../../translated_images/pt-BR/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

# Planejamento de Design

## Introdução

Esta lição abordará

* Definir um objetivo geral claro e dividir uma tarefa complexa em tarefas gerenciáveis.
* Aproveitar saída estruturada para respostas mais confiáveis e legíveis por máquina.
* Aplicar uma abordagem orientada a eventos para lidar com tarefas dinâmicas e entradas inesperadas.

## Objetivos de Aprendizagem

Após concluir esta lição, você terá compreensão sobre:

* Identificar e definir um objetivo geral para um agente de IA, garantindo que ele saiba claramente o que precisa ser alcançado.
* Decompor uma tarefa complexa em subtarefas gerenciáveis e organizá-las em uma sequência lógica.
* Equipar agentes com as ferramentas certas (por exemplo, ferramentas de busca ou análise de dados), decidir quando e como usá-las e lidar com situações inesperadas que surgirem.
* Avaliar os resultados das subtarefas, medir desempenho e iterar as ações para melhorar a saída final.

## Definindo o Objetivo Geral e Quebrando uma Tarefa

![Definindo Objetivos e Tarefas](../../../translated_images/pt-BR/defining-goals-tasks.d70439e19e37c47a.webp)

A maioria das tarefas do mundo real é complexa demais para ser enfrentada em um único passo. Um agente de IA precisa de um objetivo conciso para guiar seu planejamento e ações. Por exemplo, considere o objetivo:

    "Gerar um itinerário de viagem para 3 dias."

Embora seja simples de declarar, ainda precisa de refinamento. Quanto mais claro o objetivo, melhor o agente (e quaisquer colaboradores humanos) podem se concentrar em alcançar o resultado correto, como criar um itinerário abrangente com opções de voo, recomendações de hotel e sugestões de atividades.

### Decomposição da Tarefa

Tarefas grandes ou complexas tornam-se mais gerenciáveis quando divididas em subtarefas menores, orientadas por objetivos.
No exemplo do itinerário de viagem, você poderia decompor o objetivo em:

* Reserva de Voos
* Reserva de Hotel
* Aluguel de Carro
* Personalização

Cada subtarefa pode então ser realizada por agentes ou processos dedicados. Um agente pode se especializar em buscar as melhores ofertas de voo, outro foca na reserva de hotéis, e assim por diante. Um agente coordenador ou “downstream” pode então compilar esses resultados em um itinerário coeso para o usuário final.

Essa abordagem modular também permite aprimoramentos incrementais. Por exemplo, você poderia adicionar agentes especializados para Recomendações de Alimentação ou Sugestões de Atividades Locais e refinar o itinerário ao longo do tempo.

### Saída Estruturada

Grandes Modelos de Linguagem (LLMs) podem gerar saídas estruturadas (por exemplo, JSON) que são mais fáceis para agentes ou serviços posteriores analisarem e processarem. Isso é especialmente útil em um contexto multiagente, onde podemos executar essas tarefas após a saída do planejamento ser recebida.

O trecho de código Python a seguir demonstra um agente planejador simples decompondo um objetivo em subtarefas e gerando um plano estruturado:

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

### Agente Planejador com Orquestração Multiagente

Neste exemplo, um Agente Roteador Semântico recebe uma solicitação do usuário (por exemplo, "Preciso de um plano de hotel para minha viagem.").

O planejador então:

* Recebe o Plano de Hotel: O planejador pega a mensagem do usuário e, com base em uma instrução do sistema (incluindo detalhes dos agentes disponíveis), gera um plano de viagem estruturado.
* Lista Agentes e suas Ferramentas: O registro de agentes contém uma lista de agentes (por exemplo, para voo, hotel, aluguel de carro e atividades) junto com as funções ou ferramentas que eles oferecem.
* Roteia o Plano para os Agentes Correspondentes: Dependendo do número de subtarefas, o planejador envia a mensagem diretamente a um agente dedicado (em cenários de tarefa única) ou coordena via um gerente de grupo de chat para colaboração multiagente.
* Resume o Resultado: Finalmente, o planejador resume o plano gerado para clareza.
O código Python a seguir ilustra esses passos:

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

O que segue é a saída do código anterior e você pode então usar essa saída estruturada para direcionar para `assigned_agent` e resumir o plano de viagem para o usuário final.

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

### Planejamento Iterativo

Algumas tarefas requerem um vai-e-volta ou replanejamento, onde o resultado de uma subtarefa influencia a próxima. Por exemplo, se o agente descobrir um formato de dado inesperado ao reservar voos, pode precisar adaptar sua estratégia antes de prosseguir para reservas de hotel.

Além disso, o feedback do usuário (por exemplo, um humano decidindo que prefere um voo mais cedo) pode desencadear um replanejamento parcial. Essa abordagem dinâmica e iterativa garante que a solução final esteja alinhada com as limitações do mundo real e as preferências do usuário em evolução.

por exemplo código de amostra

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. mesmo que o código anterior e passe o histórico do usuário, plano atual

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
# .. replanejar e enviar as tarefas aos agentes respectivos
```

Para um planejamento mais abrangente, confira o Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> para resolver tarefas complexas.

## Resumo

Neste artigo, examinamos um exemplo de como podemos criar um planejador que pode selecionar dinamicamente os agentes disponíveis definidos. A saída do Planejador decompõe as tarefas e atribui os agentes para que possam ser executadas. Presume-se que os agentes tenham acesso às funções/ferramentas necessárias para realizar a tarefa. Além dos agentes, você pode incluir outros padrões como reflexão, sumarizador e chat round robin para personalizar ainda mais.

## Recursos Adicionais

Magentic One - Um sistema multiagente generalista para resolver tarefas complexas e que alcançou resultados impressionantes em múltiplos benchmarks desafiadores de agentes. Referência: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. Nesta implementação, o orquestrador cria planos específicos para tarefas e delega essas tarefas aos agentes disponíveis. Além do planejamento, o orquestrador também emprega um mecanismo de rastreamento para monitorar o progresso da tarefa e replanejar conforme necessário.

### Tem mais perguntas sobre o Padrão de Design de Planejamento?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrar outros aprendizes, participar de horas de atendimento e tirar suas dúvidas sobre Agentes de IA.

## Lição Anterior

[Construindo Agentes de IA Confiáveis](../06-building-trustworthy-agents/README.md)

## Próxima Lição

[Padrão de Design Multiagente](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->