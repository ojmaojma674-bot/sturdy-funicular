package com.vhotiex.model

import androidx.compose.runtime.Immutable

@Immutable
data class AgentProfile(
    val name: String,
    val role: String,
    val tone: String,
    val energy: String,
    val empathy: Float,
    val reliability: Float,
    val specialties: List<String>,
    val collaborators: List<String>
)

@Immutable
data class ChatMessage(
    val text: String,
    val sender: String,
    val isUser: Boolean
)
