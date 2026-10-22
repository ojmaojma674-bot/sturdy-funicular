package com.vhotiex.ui.chat

import androidx.lifecycle.ViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow

class ChatViewModel : ViewModel() {
    private val _messages = MutableStateFlow<List<String>>(emptyList())
    val messages: StateFlow<List<String>> = _messages

    fun sendMessage(text: String) {
        if (text.isBlank()) return
        val current = _messages.value.toMutableList()
        current.add(text)
        _messages.value = current
    }
}
