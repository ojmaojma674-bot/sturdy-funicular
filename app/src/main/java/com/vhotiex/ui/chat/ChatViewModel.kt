package com.vhotiex.ui.chat

import androidx.lifecycle.ViewModel
import com.vhotiex.model.ChatMessage
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow

class ChatViewModel : ViewModel() {
    private val _messages = MutableStateFlow<List<ChatMessage>>(emptyList())
    val messages: StateFlow<List<ChatMessage>> = _messages

    fun sendMessage(text: String, agentName: String = "Astra") {
        if (text.isBlank()) return

        val userMessage = ChatMessage(text = text, sender = "You", isUser = true)
        val responseText = buildAgentResponse(agentName, text)
        val agentReply = ChatMessage(text = responseText, sender = agentName, isUser = false)

        _messages.value = _messages.value + listOf(userMessage, agentReply)
    }

    private fun buildAgentResponse(agentName: String, userInput: String): String {
        val normalizedInput = userInput.trim()
        val base = when (agentName) {
            "Nova" -> "Nova is gathering the latest context and cross-checking facts before answering."
            "Orion" -> "Orion is mapping this into a clean technical plan and prioritizing practical execution."
            "Lyra" -> "Lyra is shaping this into a polished, human-friendly response with strong clarity."
            "Sable" -> "Sable is reviewing risks, edge cases, and quality concerns before finalizing the answer."
            "Kite" -> "Kite is organizing this into a structured roadmap and next-step sequence."
            "Quill" -> "Quill is analyzing patterns and extracting the key insight behind the request."
            "Echo" -> "Echo is responding with empathy, tone, and conversational clarity."
            else -> "Astra is coordinating the team and giving you a clear, balanced answer."
        }

        return "$base You asked: \"$normalizedInput\". I’ve routed this through the ${agentName} workflow and kept the answer direct, useful, and human-centered."
    }
}
