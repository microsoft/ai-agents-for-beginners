<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:18:04+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "pt"
}
-->
# Aula 11: Integração com o Protocolo de Contexto de Modelo (MCP)

## Introdução ao Protocolo de Contexto de Modelo (MCP)

O Protocolo de Contexto de Modelo (MCP) é uma estrutura inovadora projetada para padronizar as interações entre modelos de IA e aplicações cliente. O MCP atua como uma ponte entre os modelos de IA e as aplicações que os utilizam, fornecendo uma interface consistente, independentemente da implementação subjacente do modelo.

Principais aspetos do MCP:

- **Comunicação Padronizada**: O MCP estabelece uma linguagem comum para as aplicações comunicarem com os modelos de IA  
- **Gestão de Contexto Aprimorada**: Permite a passagem eficiente de informações contextuais para os modelos de IA  
- **Compatibilidade Multiplataforma**: Funciona em várias linguagens de programação, incluindo C#, Java, JavaScript, Python e TypeScript  
- **Integração Simplificada**: Facilita a integração de diferentes modelos de IA nas aplicações  

O MCP é particularmente valioso no desenvolvimento de agentes de IA, pois permite que os agentes interajam com vários sistemas e fontes de dados através de um protocolo unificado, tornando-os mais flexíveis e poderosos.

## Objetivos de Aprendizagem
- Compreender o que é o MCP e o seu papel no desenvolvimento de agentes de IA  
- Configurar e configurar um servidor MCP para integração com o GitHub  
- Construir um sistema multiagente utilizando ferramentas MCP  
- Implementar RAG (Geração Aumentada por Recuperação) com o Azure Cognitive Search  

## Pré-requisitos
- Python 3.8+  
- Node.js 14+  
- Subscrição do Azure  
- Conta no GitHub  
- Conhecimentos básicos sobre o Semantic Kernel  

## Instruções de Configuração

1. **Configuração do Ambiente**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configurar Serviços do Azure**  
   - Criar um recurso do Azure Cognitive Search  
   - Configurar o serviço Azure OpenAI  
   - Definir variáveis de ambiente no `.env`  

3. **Configuração do Servidor MCP**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Estrutura do Projeto

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## Componentes Principais

### 1. Sistema Multiagente
- Agente GitHub: Análise de repositórios  
- Agente Hackathon: Recomendações de projetos  
- Agente de Eventos: Sugestões de eventos tecnológicos  

### 2. Integração com o Azure
- Cognitive Search para indexação de eventos  
- Azure OpenAI para inteligência dos agentes  
- Implementação do padrão RAG  

### 3. Ferramentas MCP
- Análise de repositórios GitHub  
- Inspeção de código  
- Extração de metadados  

## Análise do Código

O exemplo demonstra:  
1. Integração com o servidor MCP  
2. Orquestração de múltiplos agentes  
3. Integração com o Azure Cognitive Search  
4. Implementação do padrão RAG  

Funcionalidades principais:  
- Análise em tempo real de repositórios GitHub  
- Recomendações inteligentes de projetos  
- Correspondência de eventos utilizando o Azure Search  
- Respostas em streaming com Chainlit  

## Executar o Exemplo

Para instruções detalhadas de configuração e mais informações, consulte o [README do Exemplo de Servidor MCP no GitHub](./code_samples/github-mcp/README.md).

1. Iniciar o servidor MCP:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Lançar a aplicação:  
   ```bash
   chainlit run app.py -w
   ```

3. Testar a integração:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Resolução de Problemas

Problemas comuns e soluções:  
1. Problemas de Conexão com o MCP  
   - Verifique se o servidor está em execução  
   - Confirme a disponibilidade da porta  
   - Valide os tokens do GitHub  

2. Problemas com o Azure Search  
   - Verifique as cadeias de conexão  
   - Confirme a existência do índice  
   - Valide o carregamento de documentos  

## Próximos Passos
- Explorar ferramentas adicionais do MCP  
- Implementar agentes personalizados  
- Melhorar as capacidades do RAG  
- Adicionar mais fontes de eventos  
- **Avançado**: Consulte [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) para exemplos de comunicação entre agentes  

## Recursos
- [MCP para Iniciantes](https://aka.ms/mcp-for-beginners)  
- [Documentação do MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Documentação do Azure Cognitive Search](https://learn.microsoft.com/azure/search/)  
- [Guias do Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)  

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.