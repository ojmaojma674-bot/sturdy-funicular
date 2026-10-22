package com.vhotiex.ui.chat

import androidx.lifecycle.ViewModel
import com.vhotiex.model.ChatMessage
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow

class ChatViewModel : ViewModel() {
    private val _messages = MutableStateFlow<List<ChatMessage>>(listOf(
        ChatMessage(
            text = "Astra is online and ready to coordinate the team.",
            sender = "Astra",
            isUser = false
        ),
        ChatMessage(
            text = "Orion is checking code quality and system stability.",
            sender = "Orion",
            isUser = false
        ),
        ChatMessage(
            text = "I want a premium AI assistant app with a proper dashboard.",
            sender = "You",
            isUser = true
        )
    ))
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
            "Nova" -> "Nova is gathering the latest context and checking reliability before responding."
            "Orion" -> "Orion is mapping this into a clean technical plan with practical execution priorities."
            "Lyra" -> "Lyra is shaping this into a polished, human-friendly response."
            "Sable" -> "Sable is reviewing risks, quality concerns, and edge cases."
            "Kite" -> "Kite is organizing the work into a clear roadmap and next steps."
            "Quill" -> "Quill is extracting the most valuable insight and patterns from your request."
            "Echo" -> "Echo is replying with empathy and conversation-first clarity."
            else -> "Astra is coordinating the team and delivering a clear, balanced answer."
        }

        return "$base You asked: \"$normalizedInput\". I’ve routed this through the ${agentName} workflow and kept it useful, direct, and human-centered."
    }
}
