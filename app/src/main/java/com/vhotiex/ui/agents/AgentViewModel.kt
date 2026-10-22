package com.vhotiex.ui.agents

import androidx.lifecycle.ViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow

class AgentViewModel : ViewModel() {
    private val _selectedAgent = MutableStateFlow("Astra")
    val selectedAgent: StateFlow<String> = _selectedAgent

    fun selectAgent(agent: String) {
        if (agent.isNotBlank()) {
            _selectedAgent.value = agent
        }
    }
}
