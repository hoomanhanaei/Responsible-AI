# Model card for "C4AI Command R+"

Created in accordance with [model cards paper](https://arxiv.org/pdf/1810.03993)

Jump to section:

- [Model overview](#model-overview)
- [Data provenance](#data-provenance)
- [Performance](#performance)
- [Limitations](#limitations)
- [Ideas on Data and Model Governance](#ideas-on-data-and-model-governance)

## Model overview
- **C4AI Command R+:**<br>- Is an open weights research release of a 104 billion parameter large language model (LLM) designed for advanced natural language processing (NLP) tasks, and is also part of a family of open weight releases from `Cohere For AI` and `Cohere`.<br>- It is Built on the transformer architecture, this model excels in text understanding, generation, and other complex (NLP) tasks. Its large parameter size allows it to capture more nuanced relationships and patterns within text, making it powerful for tasks requiring high levels of comprehension and fluency ([more](https://huggingface.co/CohereForAI/c4ai-command-r-plus-4bit)).

- **This Model performs:**<br>- Various natural language processing (NLP) tasks, including *text generation*, *summarization*, *translation*, and *question answering*. Its architecture allows it to understand and generate human-like text based on the context provided, making it suitable for a range of applications in conversational AI, and content creation.

- **Intended Use Cases:**<br>- `Generate text and code:` The model’s grounded generation capabilities allows to generate text and code based on a list of supplied document snippets.<br>- `Automate complex tasks:` The model’s tool and multihop capabilities allows to automate complex tasks that require multiple steps.<br>- `Improve language understanding:` Use the model’s multilingual support to improve language understanding and respond to users in different languages ([Use-cases](https://dataloop.ai/library/model/cohereforai_c4ai-command-r-plus-4bit/)).

- **Potential missuses:**<br>- `Reduced Censorship on NSFW Content` makes Command R+ capable of handling NSFW storytelling with less resistance, providing responses readily in these contexts. This increased flexibility could be exploited to generate inappropriate or harmful content ([NSFW and Censorship](https://llm.extractum.io/static/blog/?id=command-r-plus-discussions)).

## Data provenance
- `C4AI Command R+` was trained on a vast and diverse corpus of text data, comprising of but limited to:<br>A- datasets that include instructions for using various tools, enabling it to understand and execute user commands effectively.<br> B- diverse conversational scenarios where tool use is required, helping the model learn appropriate responses and actions.<br>- The model is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, Simplified Chinese, and Arabic.<br>- Pre-training data additionally included the following 13 languages: Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, Persian. ([Cohere docs](https://docs.cohere.com/docs/command-r-plus), [Hugging face](https://huggingface.co/CohereForAI/c4ai-command-r-plus-4bit)).

- Like all AI models, C4AI Command R+ may reflect **biases and prejudices** present in the data it was trained on. The model performs well only on 10 languages which may include, cultural, gender, racial, and political biases inherent in the text sources, which can lead to biased outputs.<br>Potential underrepresentation of minority languages or dialects which may introduce bias to model responses which concerns these languages. (`To list precise model baises, accurate scrutinizing of training data is required.`)

## Performance
- **Performance metrics** for the model were not available. No specific performance metric was mentioned in model documentation.<br>Although common metrics to measure the accuracy of LLM could be employed.<br>- `Perplexity` To assess how well the model predicts a sample.<br>- `Generative Quality` Assess coherence and fluency with BLEU and ROUGE metrics.<br>- `Accuracy` by using benchmarks like GLUE.<br>- `RAI (Responsible AI)` Is also a crucial metric to ensure ethical use and mitigate potential risks, which can be applied using pre-designed questions in different RAI categories.<br>- *these could be measured specificly for goals intented to achieve using the model.*
- **Results for different demographic groups** is not available. However since it only performs well on 10 languages, it is crucial to evaluate its output based on cultural contetxt.

## Limitations
- The immediate applicability of this model `“out of the box”` may be constrained for specific requirements. For instance, It might not perform well out-of-the-box for pure code completion ([Hugging face](https://huggingface.co/CohereForAI/c4ai-command-r-plus-4bit)).
- **Structured Input Requirments**: The model expects document snippets to be relatively short (100-400 words per chunk). This imposes a constraint on the type of content that can be effectively processed. Longer documents need to be broken down into smaller chunks, which can lead to `Loss of Context` & `Increased Complexity`.
- **Impact on User Experience:** May limit responsiveness and require a learning curve for effective use.
- **Dependency on User-Supplied Preambles:** Introduce variability and a potential barrier for non-expert users.
- **Computational Requirements:** The large size of the model necessitates significant computational resources, limiting accessibility for smaller organizations and applications ([Hugging face](https://huggingface.co/CohereForAI/c4ai-command-r-plus-4bit)).

## Ideas on Data and Model Governance
- **How data provenance will be tracked in future iterations?**<br>-`Data Version Control (DVC):` DVC does not store the actual data within the version control system, its approach to managing metadata and leveraging remote storage services provides a robust framework for tracking data provenance from its **metadata**.
- **How updates and version control of the model will be handled for transparency?**<br>- Using a formal `versioning system` to manage updates to the model, ensuring that each new release is documented and previous versions remain accessible.<br>- Continuous `monitoring of model performance` and outputs to identify and address emerging biases or ethical concerns.<br>- including `detailed release notes` or changelogs that describe what changes were made in each version. This helps users understand the differences between versions, such as new features, improvements, bug fixes, or potential breaking changes.
