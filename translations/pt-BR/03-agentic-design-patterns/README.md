[![Como Projetar Bons Agentes de IA](../../../translated_images/pt-BR/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Clique na imagem acima para assistir ao vídeo desta aula)_
# Princípios de Design Agentic de IA

## Introdução

Existem muitas formas de pensar sobre a construção de Sistemas Agentic de IA. Dado que a ambiguidade é uma característica e não um bug no design de IA Generativa, às vezes é difícil para os engenheiros descobrirem por onde começar. Criamos um conjunto de Princípios de Design UX centrados no humano para permitir que os desenvolvedores construam sistemas agentic centrados no cliente para resolver suas necessidades de negócio. Esses princípios de design não são uma arquitetura prescritiva, mas sim um ponto de partida para equipes que estão definindo e construindo experiências agentic.

Em geral, agentes devem:

- Ampliar e escalar capacidades humanas (brainstorming, resolução de problemas, automação, etc.)
- Preencher lacunas de conhecimento (me atualizar sobre domínios de conhecimento, tradução, etc.)
- Facilitar e apoiar a colaboração nas formas que preferimos trabalhar com os outros
- Fazer de nós versões melhores de nós mesmos (ex.: coach pessoal/gestor de tarefas, ajudando a aprender regulação emocional e habilidades de mindfulness, construir resiliência, etc.)

## Esta Aula Vai Cobrir

- O que são os Princípios de Design Agentic
- Quais diretrizes seguir ao implementar esses princípios de design
- Exemplos de uso dos princípios de design

## Objetivos de Aprendizagem

Após concluir esta aula, você será capaz de:

1. Explicar o que são os Princípios de Design Agentic
2. Explicar as diretrizes para uso dos Princípios de Design Agentic
3. Entender como construir um agente usando os Princípios de Design Agentic

## Os Princípios de Design Agentic

![Princípios de Design Agentic](../../../translated_images/pt-BR/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agente (Espaço)

Este é o ambiente no qual o agente opera. Esses princípios informam como projetamos agentes para atuar nos mundos físicos e digitais.

- **Conectar, não colapsar** – ajudar a conectar pessoas a outras pessoas, eventos e conhecimento acionável para possibilitar colaboração e conexão.
- Agentes ajudam a conectar eventos, conhecimento e pessoas.
- Agentes aproximam as pessoas. Não são projetados para substituir ou diminuir as pessoas.
- **Facilmente acessível, mas ocasionalmente invisível** – o agente basicamente opera em segundo plano e só nos lembra quando é relevante e apropriado.
  - O agente é facilmente descoberto e acessível para usuários autorizados em qualquer dispositivo ou plataforma.
  - O agente suporta entradas e saídas multimodais (som, voz, texto, etc.).
  - O agente pode transitar suavemente entre primeiro plano e segundo plano; entre proativo e reativo, dependendo da percepção das necessidades do usuário.
  - O agente pode operar em forma invisível, mas seu processo em segundo plano e colaboração com outros agentes são transparentes e controláveis pelo usuário.

### Agente (Tempo)

Este é o modo como o agente opera ao longo do tempo. Esses princípios informam como projetamos agentes que interagem com passado, presente e futuro.

- **Passado**: Refletindo sobre uma história que inclui estado e contexto.
  - O agente fornece resultados mais relevantes baseados na análise de dados históricos mais abrangentes além do evento, pessoas ou estados.
  - O agente cria conexões a partir de eventos passados e reflete ativamente na memória para interagir com situações atuais.
- **Agora**: Incentivar mais do que notificar.
  - O agente incorpora uma abordagem abrangente para interagir com pessoas. Quando um evento acontece, o agente vai além da simples notificação ou formalidade estática. O agente pode simplificar fluxos ou gerar dinamicamente dicas para direcionar a atenção do usuário no momento certo.
  - O agente entrega informações baseadas no ambiente contextual, mudanças sociais e culturais e adaptadas à intenção do usuário.
  - A interação com o agente pode ser gradual, evoluindo/ crescendo em complexidade para capacitar os usuários a longo prazo.
- **Futuro**: Adaptar e evoluir.
  - O agente se adapta a vários dispositivos, plataformas e modalidades.
  - O agente se adapta ao comportamento do usuário, necessidades de acessibilidade e é totalmente personalizável.
  - O agente é moldado e evolui através da interação contínua com o usuário.

### Agente (Núcleo)

Estes são os elementos-chave no núcleo do design do agente.

- **Aceite a incerteza, mas estabeleça confiança**.
  - Um certo nível de incerteza do agente é esperado. A incerteza é um elemento chave do design do agente.
  - Confiança e transparência são camadas fundamentais do design do agente.
  - Humanos controlam quando o agente está ligado/desligado e o status do agente é claramente visível em todos os momentos.

## Diretrizes para Implementar Estes Princípios

Quando usar os princípios de design anteriores, siga as diretrizes a seguir:

1. **Transparência**: Informe o usuário que IA está envolvida, como ela funciona (incluindo ações passadas), e como fornecer feedback e modificar o sistema.
2. **Controle**: Permita que o usuário personalize, especifique preferências e personalize, e tenha controle sobre o sistema e seus atributos (incluindo a habilidade de esquecer).
3. **Consistência**: Busque experiências consistentes e multimodais em dispositivos e terminais. Use elementos UI/UX familiares sempre que possível (ex.: ícone de microfone para interação por voz) e reduza a carga cognitiva do cliente ao máximo (ex.: respostas concisas, auxílios visuais e conteúdo 'Saiba Mais').

## Como Projetar um Agente de Viagens usando Estes Princípios e Diretrizes

Imagine que você está projetando um Agente de Viagens, aqui está como você poderia pensar em usar os Princípios de Design e Diretrizes:

1. **Transparência** – Informe o usuário que o Agente de Viagens é um Agente habilitado por IA. Forneça algumas instruções básicas sobre como começar (ex.: uma mensagem de “Olá”, prompts de exemplo). Documente claramente isso na página do produto. Mostre a lista de prompts que o usuário fez no passado. Deixe claro como fornecer feedback (joinha e sinal negativo, botão Enviar Feedback, etc.). Articule claramente se o agente tem restrições de uso ou tópicos.
2. **Controle** – Certifique-se de que está claro como o usuário pode modificar o agente após ele ter sido criado com coisas como o Prompt do Sistema. Permita que o usuário escolha o nível de verbosidade do agente, seu estilo de escrita, e quaisquer ressalvas sobre o que o agente não deve falar. Permita que o usuário veja e apague quaisquer arquivos ou dados associados, prompts e conversas passadas.
3. **Consistência** – Certifique-se de que os ícones para Compartilhar Prompt, adicionar um arquivo ou foto e marcar alguém ou algo são padrão e reconhecíveis. Use o ícone de clipe de papel para indicar envio/compartilhamento de arquivos com o agente, e um ícone de imagem para indicar upload de gráficos.

## Códigos de Exemplo

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Quer Saber Mais sobre Padrões de Design Agentic de IA?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrar outros aprendizes, participar de horários de atendimento e tirar suas dúvidas sobre Agentes de IA.

## Recursos Adicionais

- <a href="https://openai.com" target="_blank">Práticas para Governança de Sistemas Agentic de IA | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">Projeto HAX Toolkit - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Caixa de Ferramentas de IA Responsável</a>

## Aula Anterior

[Explorando Frameworks Agentic](../02-explore-agentic-frameworks/README.md)

## Próxima Aula

[Padrão de Design de Uso de Ferramentas](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->