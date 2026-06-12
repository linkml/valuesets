"""
Frontier AI Model Value Sets

A hierarchical value set of frontier large language / foundation models, organized as provider > model family > specific model release. Leaf nodes use the canonical model identifier as used in the providers' APIs and "/model" selectors (e.g. claude-opus-4-8, gpt-5.5, gemini-3.5-flash). Intermediate nodes group models by developer and family. Per-model metadata (knowledge/training cutoff, context window, max output tokens, release date, links to model cards) is attached as annotations and see_also links where available.
NOTE: The frontier model landscape changes rapidly; values reflect the state of provider documentation as of mid-2026. Canonical API identifiers for open-weight models (Llama, DeepSeek, Mistral, Kimi) can vary between inference hosts; the identifiers given are the developer's reference names.

Generated from: computing/frontier_ai_models.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class FrontierModelEnum(RichEnum):
    """
    Hierarchical enumeration of frontier AI models. The hierarchy has three tiers: developer (e.g. ANTHROPIC), model family (e.g. CLAUDE_OPUS), and specific model release identified by its canonical API model id (e.g. claude-opus-4-8). Intermediate developer and family nodes are uppercase categorical values; leaf nodes are the verbatim API identifiers.
    """
    # Enum members
    ANTHROPIC = "ANTHROPIC"
    CLAUDE_OPUS = "CLAUDE_OPUS"
    CLAUDE_OPUS_4_8 = "claude-opus-4-8"
    CLAUDE_OPUS_4_7 = "claude-opus-4-7"
    CLAUDE_OPUS_4_6 = "claude-opus-4-6"
    CLAUDE_OPUS_4_5 = "claude-opus-4-5"
    CLAUDE_SONNET = "CLAUDE_SONNET"
    CLAUDE_SONNET_4_6 = "claude-sonnet-4-6"
    CLAUDE_SONNET_4_5 = "claude-sonnet-4-5"
    CLAUDE_HAIKU = "CLAUDE_HAIKU"
    CLAUDE_HAIKU_4_5 = "claude-haiku-4-5"
    CLAUDE_FABLE = "CLAUDE_FABLE"
    CLAUDE_FABLE_5 = "claude-fable-5"
    CLAUDE_MYTHOS = "CLAUDE_MYTHOS"
    CLAUDE_MYTHOS_5 = "claude-mythos-5"
    OPENAI = "OPENAI"
    GPT_5 = "GPT_5"
    GPT_5_5 = "gpt-5.5"
    GPT_5_4 = "gpt-5.4"
    GPT_5_4_MINI = "gpt-5.4-mini"
    GPT_5_2 = "gpt-5.2"
    GPT_5_2_CODEX = "gpt-5.2-codex"
    GOOGLE = "GOOGLE"
    GEMINI_3 = "GEMINI_3"
    GEMINI_3_5_FLASH = "gemini-3.5-flash"
    GEMINI_3_1_PRO_PREVIEW = "gemini-3.1-pro-preview"
    GEMINI_3_FLASH_PREVIEW = "gemini-3-flash-preview"
    GEMINI_3_1_FLASH_LITE = "gemini-3.1-flash-lite"
    GEMINI_2_5 = "GEMINI_2_5"
    GEMINI_2_5_PRO = "gemini-2.5-pro"
    GEMINI_2_5_FLASH = "gemini-2.5-flash"
    GEMINI_2_5_FLASH_LITE = "gemini-2.5-flash-lite"
    XAI = "XAI"
    GROK_4 = "GROK_4"
    GROK_4_3 = "grok-4.3"
    GROK_4_20_0309_REASONING = "grok-4.20-0309-reasoning"
    GROK_4_0709 = "grok-4-0709"
    GROK_CODE = "GROK_CODE"
    GROK_CODE_FAST_1 = "grok-code-fast-1"
    META = "META"
    LLAMA_4 = "LLAMA_4"
    LLAMA_4_MAVERICK = "llama-4-maverick"
    LLAMA_4_SCOUT = "llama-4-scout"
    DEEPSEEK = "DEEPSEEK"
    DEEPSEEK_MODELS = "DEEPSEEK_MODELS"
    DEEPSEEK_CHAT = "deepseek-chat"
    DEEPSEEK_REASONER = "deepseek-reasoner"
    MISTRAL = "MISTRAL"
    MISTRAL_LARGE = "MISTRAL_LARGE"
    MISTRAL_LARGE_3 = "mistral-large-3"
    MOONSHOT = "MOONSHOT"
    KIMI = "KIMI"
    KIMI_K2_6 = "kimi-k2.6"

# Set metadata after class creation
FrontierModelEnum._metadata = {
    "ANTHROPIC": {'description': 'Models developed by Anthropic (the Claude family)', 'annotations': {'node_type': 'developer', 'homepage': 'https://www.anthropic.com'}},
    "CLAUDE_OPUS": {'description': "Claude Opus - Anthropic's most capable Opus-tier model family", 'annotations': {'node_type': 'family', 'tier': 'most capable'}},
    "CLAUDE_OPUS_4_8": {'description': "Claude Opus 4.8 - Anthropic's most capable Opus-tier model; highly autonomous, state-of-the-art on long-horizon agentic work, knowledge work, and memory. Adaptive thinking only.", 'annotations': {'node_type': 'model', 'api_model_id': 'claude-opus-4-8', 'developer': 'Anthropic', 'context_window': 1000000, 'max_output_tokens': 128000, 'input_usd_per_mtok': 5.0, 'output_usd_per_mtok': 25.0}, 'aliases': ['Opus 4.8', 'opus']},
    "CLAUDE_OPUS_4_7": {'description': 'Claude Opus 4.7 - previous-generation Opus; highly autonomous, strong on long-horizon agentic work, vision, and memory. Adaptive thinking only.', 'annotations': {'node_type': 'model', 'api_model_id': 'claude-opus-4-7', 'developer': 'Anthropic', 'context_window': 1000000, 'max_output_tokens': 128000}, 'aliases': ['Opus 4.7']},
    "CLAUDE_OPUS_4_6": {'description': 'Claude Opus 4.6 - older Opus model supporting adaptive thinking and 128K max output tokens.', 'annotations': {'node_type': 'model', 'api_model_id': 'claude-opus-4-6', 'developer': 'Anthropic', 'context_window': 1000000, 'max_output_tokens': 128000}, 'aliases': ['Opus 4.6']},
    "CLAUDE_OPUS_4_5": {'description': 'Claude Opus 4.5 - legacy Opus model (still active).', 'annotations': {'node_type': 'model', 'api_model_id': 'claude-opus-4-5', 'full_model_id': 'claude-opus-4-5-20251101', 'developer': 'Anthropic'}, 'aliases': ['Opus 4.5']},
    "CLAUDE_SONNET": {'description': "Claude Sonnet - Anthropic's balanced speed / intelligence family", 'annotations': {'node_type': 'family', 'tier': 'balanced'}},
    "CLAUDE_SONNET_4_6": {'description': "Claude Sonnet 4.6 - Anthropic's best combination of speed and intelligence. Supports adaptive thinking.", 'annotations': {'node_type': 'model', 'api_model_id': 'claude-sonnet-4-6', 'developer': 'Anthropic', 'context_window': 1000000, 'max_output_tokens': 64000, 'input_usd_per_mtok': 3.0, 'output_usd_per_mtok': 15.0}, 'aliases': ['Sonnet 4.6', 'sonnet']},
    "CLAUDE_SONNET_4_5": {'description': 'Claude Sonnet 4.5 - legacy Sonnet model (still active).', 'annotations': {'node_type': 'model', 'api_model_id': 'claude-sonnet-4-5', 'full_model_id': 'claude-sonnet-4-5-20250929', 'developer': 'Anthropic'}, 'aliases': ['Sonnet 4.5']},
    "CLAUDE_HAIKU": {'description': "Claude Haiku - Anthropic's fastest and most cost-effective family", 'annotations': {'node_type': 'family', 'tier': 'fast'}},
    "CLAUDE_HAIKU_4_5": {'description': "Claude Haiku 4.5 - Anthropic's fastest and most cost-effective model for simple, latency-sensitive tasks.", 'annotations': {'node_type': 'model', 'api_model_id': 'claude-haiku-4-5', 'full_model_id': 'claude-haiku-4-5-20251001', 'developer': 'Anthropic', 'context_window': 200000, 'max_output_tokens': 64000, 'input_usd_per_mtok': 1.0, 'output_usd_per_mtok': 5.0}, 'aliases': ['Haiku 4.5', 'haiku']},
    "CLAUDE_FABLE": {'description': "Claude Fable - Anthropic's most capable widely released model family, for the most demanding reasoning and long-horizon agentic work.", 'annotations': {'node_type': 'family', 'tier': 'frontier'}},
    "CLAUDE_FABLE_5": {'description': "Claude Fable 5 - Anthropic's most capable widely released model. Thinking is always on; raw chain of thought is never returned. Requires 30-day data retention.", 'annotations': {'node_type': 'model', 'api_model_id': 'claude-fable-5', 'developer': 'Anthropic', 'context_window': 1000000, 'max_output_tokens': 128000, 'input_usd_per_mtok': 10.0, 'output_usd_per_mtok': 50.0}, 'aliases': ['Fable 5', 'fable']},
    "CLAUDE_MYTHOS": {'description': 'Claude Mythos - same capabilities and API behavior as Claude Fable, available exclusively through Project Glasswing.', 'annotations': {'node_type': 'family', 'tier': 'frontier', 'availability': 'Project Glasswing only'}},
    "CLAUDE_MYTHOS_5": {'description': 'Claude Mythos 5 - same capabilities, pricing, limits, and API behavior as Claude Fable 5; available only through Project Glasswing.', 'annotations': {'node_type': 'model', 'api_model_id': 'claude-mythos-5', 'developer': 'Anthropic', 'context_window': 1000000, 'max_output_tokens': 128000}, 'aliases': ['Mythos 5']},
    "OPENAI": {'description': 'Models developed by OpenAI (the GPT family)', 'annotations': {'node_type': 'developer', 'homepage': 'https://openai.com'}},
    "GPT_5": {'description': "GPT-5 - OpenAI's frontier model family for coding and professional work", 'annotations': {'node_type': 'family', 'tier': 'frontier'}},
    "GPT_5_5": {'description': 'GPT-5.5 - OpenAI\'s newest frontier model, "a new class of intelligence for coding and professional work".', 'annotations': {'node_type': 'model', 'api_model_id': 'gpt-5.5', 'developer': 'OpenAI', 'training_cutoff': '2025-12-01', 'context_window': 1000000}, 'aliases': ['GPT-5.5']},
    "GPT_5_4": {'description': 'GPT-5.4 - a more affordable model for coding and professional work.', 'annotations': {'node_type': 'model', 'api_model_id': 'gpt-5.4', 'developer': 'OpenAI', 'training_cutoff': '2025-08-31', 'context_window': 1000000}, 'aliases': ['GPT-5.4']},
    "GPT_5_4_MINI": {'description': "GPT-5.4 mini - OpenAI's strongest mini model for coding, computer use, and subagents; lower latency and cost.", 'annotations': {'node_type': 'model', 'api_model_id': 'gpt-5.4-mini', 'developer': 'OpenAI', 'training_cutoff': '2025-08-31', 'context_window': 400000}, 'aliases': ['GPT-5.4 mini']},
    "GPT_5_2": {'description': 'GPT-5.2 - previous frontier model for complex professional work.', 'annotations': {'node_type': 'model', 'api_model_id': 'gpt-5.2', 'developer': 'OpenAI'}, 'aliases': ['GPT-5.2']},
    "GPT_5_2_CODEX": {'description': 'GPT-5.2-Codex - coding-specialized variant for API-authenticated Codex workflows.', 'annotations': {'node_type': 'model', 'api_model_id': 'gpt-5.2-codex', 'developer': 'OpenAI', 'specialization': 'coding'}, 'aliases': ['GPT-5.2 Codex']},
    "GOOGLE": {'description': 'Models developed by Google DeepMind (the Gemini family)', 'annotations': {'node_type': 'developer', 'homepage': 'https://deepmind.google'}},
    "GEMINI_3": {'description': "Gemini 3 - Google's latest generation multimodal model family", 'annotations': {'node_type': 'family', 'tier': 'frontier'}},
    "GEMINI_3_5_FLASH": {'description': "Gemini 3.5 Flash - Google's most intelligent model for agentic and coding tasks, delivering near-Pro intelligence at Flash-tier speed and cost.", 'annotations': {'node_type': 'model', 'api_model_id': 'gemini-3.5-flash', 'developer': 'Google DeepMind', 'release_date': '2026-05-19', 'context_window': 1000000}, 'aliases': ['Gemini 3.5 Flash']},
    "GEMINI_3_1_PRO_PREVIEW": {'description': 'Gemini 3.1 Pro - reasoning-first model optimized for complex agentic workflows and coding, with adaptive thinking and integrated grounding.', 'annotations': {'node_type': 'model', 'api_model_id': 'gemini-3.1-pro-preview', 'developer': 'Google DeepMind', 'context_window': 1000000}, 'aliases': ['Gemini 3.1 Pro']},
    "GEMINI_3_FLASH_PREVIEW": {'description': 'Gemini 3 Flash - frontier-class performance at reduced cost.', 'annotations': {'node_type': 'model', 'api_model_id': 'gemini-3-flash-preview', 'developer': 'Google DeepMind'}, 'aliases': ['Gemini 3 Flash']},
    "GEMINI_3_1_FLASH_LITE": {'description': 'Gemini 3.1 Flash-Lite - most cost-efficient Gemini model, optimized for low latency and high-volume traffic.', 'annotations': {'node_type': 'model', 'api_model_id': 'gemini-3.1-flash-lite', 'developer': 'Google DeepMind'}, 'aliases': ['Gemini 3.1 Flash-Lite']},
    "GEMINI_2_5": {'description': "Gemini 2.5 - Google's previous-generation multimodal model family", 'annotations': {'node_type': 'family'}},
    "GEMINI_2_5_PRO": {'description': 'Gemini 2.5 Pro - high-capability model for complex reasoning and coding with adaptive thinking and a 1M token context.', 'annotations': {'node_type': 'model', 'api_model_id': 'gemini-2.5-pro', 'developer': 'Google DeepMind', 'context_window': 1000000}, 'aliases': ['Gemini 2.5 Pro']},
    "GEMINI_2_5_FLASH": {'description': 'Gemini 2.5 Flash - best price-performance for reasoning tasks.', 'annotations': {'node_type': 'model', 'api_model_id': 'gemini-2.5-flash', 'developer': 'Google DeepMind'}, 'aliases': ['Gemini 2.5 Flash']},
    "GEMINI_2_5_FLASH_LITE": {'description': 'Gemini 2.5 Flash-Lite - fastest and most budget-friendly option.', 'annotations': {'node_type': 'model', 'api_model_id': 'gemini-2.5-flash-lite', 'developer': 'Google DeepMind'}, 'aliases': ['Gemini 2.5 Flash-Lite']},
    "XAI": {'description': 'Models developed by xAI (the Grok family)', 'annotations': {'node_type': 'developer', 'homepage': 'https://x.ai'}},
    "GROK_4": {'description': "Grok 4 - xAI's reasoning-first flagship model family", 'annotations': {'node_type': 'family', 'tier': 'frontier'}},
    "GROK_4_3": {'description': "Grok 4.3 - xAI's reasoning-first flagship; the most intelligent and fastest model xAI has built.", 'annotations': {'node_type': 'model', 'api_model_id': 'grok-4.3', 'developer': 'xAI', 'release_date': '2026-04-30', 'context_window': 1000000}, 'aliases': ['Grok 4.3']},
    "GROK_4_20_0309_REASONING": {'description': 'Grok 4.20 (reasoning) - agentic tool-calling model noted for a very low hallucination rate.', 'annotations': {'node_type': 'model', 'api_model_id': 'grok-4.20-0309-reasoning', 'developer': 'xAI', 'context_window': 1000000}, 'aliases': ['Grok 4.20']},
    "GROK_4_0709": {'description': 'Grok 4 - earlier Grok 4 release.', 'annotations': {'node_type': 'model', 'api_model_id': 'grok-4-0709', 'developer': 'xAI', 'knowledge_cutoff': '2024-11'}, 'aliases': ['Grok 4']},
    "GROK_CODE": {'description': "Grok Code - xAI's dedicated agentic coding model family", 'annotations': {'node_type': 'family', 'specialization': 'coding'}},
    "GROK_CODE_FAST_1": {'description': 'Grok Code Fast 1 - dedicated agentic coding model.', 'annotations': {'node_type': 'model', 'api_model_id': 'grok-code-fast-1', 'developer': 'xAI', 'specialization': 'coding'}, 'aliases': ['Grok Code Fast']},
    "META": {'description': 'Open-weight models developed by Meta (the Llama family)', 'annotations': {'node_type': 'developer', 'homepage': 'https://www.llama.com', 'license': 'Llama Community License'}},
    "LLAMA_4": {'description': "Llama 4 - Meta's open-weight mixture-of-experts model family", 'annotations': {'node_type': 'family'}},
    "LLAMA_4_MAVERICK": {'description': 'Llama 4 Maverick - general-purpose open-weight chat model; highest MMLU among Llama 4 variants.', 'annotations': {'node_type': 'model', 'api_model_id': 'llama-4-maverick', 'developer': 'Meta'}, 'aliases': ['Llama 4 Maverick']},
    "LLAMA_4_SCOUT": {'description': 'Llama 4 Scout - open-weight model supporting very long context (up to 10M tokens).', 'annotations': {'node_type': 'model', 'api_model_id': 'llama-4-scout', 'developer': 'Meta', 'context_window': 10000000}, 'aliases': ['Llama 4 Scout']},
    "DEEPSEEK": {'description': 'Open-weight models developed by DeepSeek', 'annotations': {'node_type': 'developer', 'homepage': 'https://www.deepseek.com'}},
    "DEEPSEEK_MODELS": {'description': 'DeepSeek - open-weight mixture-of-experts chat and reasoning models', 'annotations': {'node_type': 'family'}},
    "DEEPSEEK_CHAT": {'description': 'DeepSeek-V3 (served as deepseek-chat) - open-weight MoE model activating ~37B of 671B parameters per token.', 'annotations': {'node_type': 'model', 'api_model_id': 'deepseek-chat', 'developer': 'DeepSeek'}, 'aliases': ['DeepSeek-V3', 'DeepSeek V3']},
    "DEEPSEEK_REASONER": {'description': 'DeepSeek-R1 (served as deepseek-reasoner) - open-weight reasoning model.', 'annotations': {'node_type': 'model', 'api_model_id': 'deepseek-reasoner', 'developer': 'DeepSeek'}, 'aliases': ['DeepSeek-R1', 'DeepSeek R1']},
    "MISTRAL": {'description': 'Models developed by Mistral AI', 'annotations': {'node_type': 'developer', 'homepage': 'https://mistral.ai'}},
    "MISTRAL_LARGE": {'description': "Mistral Large - Mistral AI's flagship open-weight model family", 'annotations': {'node_type': 'family'}},
    "MISTRAL_LARGE_3": {'description': 'Mistral Large 3 - state-of-the-art open-weight MoE model (41B active / 675B total parameters), 256K context, released under Apache 2.0.', 'annotations': {'node_type': 'model', 'api_model_id': 'mistral-large-3', 'developer': 'Mistral AI', 'release_date': '2025-12', 'context_window': 256000, 'license': 'Apache-2.0'}, 'aliases': ['Mistral Large 3']},
    "MOONSHOT": {'description': 'Models developed by Moonshot AI (the Kimi family)', 'annotations': {'node_type': 'developer', 'homepage': 'https://www.moonshot.ai'}},
    "KIMI": {'description': "Kimi - Moonshot AI's open-weight mixture-of-experts model family", 'annotations': {'node_type': 'family'}},
    "KIMI_K2_6": {'description': 'Kimi K2.6 - frontier open-weight MoE coding model (32B active / 1T total parameters).', 'annotations': {'node_type': 'model', 'api_model_id': 'kimi-k2.6', 'developer': 'Moonshot AI'}, 'aliases': ['Kimi K2.6']},
}

__all__ = [
    "FrontierModelEnum",
]