package com.vhotiex.ui.agents

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import com.vhotiex.model.AgentProfile

@Composable
fun AgentSelectorScreen(
    agentViewModel: AgentViewModel = viewModel(),
    onAgentSelected: (String) -> Unit = {}
) {
    val selectedAgent by agentViewModel.selectedAgent.collectAsState()
    val agentProfiles = listOf(
        AgentProfile("Astra", "Coordinator", "calm and visionary", "steady", 0.93f, 0.97f, listOf("planning", "alignment", "handoff"), listOf("Nova", "Lyra", "Orion")),
        AgentProfile("Nova", "Researcher", "curious and precise", "high", 0.82f, 0.90f, listOf("research", "analysis", "fact-checking"), listOf("Astra", "Quill", "Echo")),
        AgentProfile("Lyra", "Composer", "creative and warm", "sparkling", 0.94f, 0.88f, listOf("writing", "storytelling", "UX copy"), listOf("Astra", "Sable", "Kite")),
        AgentProfile("Orion", "Engineer", "structured and effective", "focused", 0.76f, 0.98f, listOf("code", "debugging", "systems"), listOf("Nova", "Echo", "Astra")),
        AgentProfile("Echo", "Communicator", "empathetic and intuitive", "adaptive", 0.96f, 0.90f, listOf("conversation", "translation", "support"), listOf("Lyra", "Nova", "Sable")),
        AgentProfile("Sable", "Reviewer", "honest and sharp", "balanced", 0.80f, 0.96f, listOf("quality assurance", "risk review", "policies"), listOf("Astra", "Orion", "Echo")),
        AgentProfile("Kite", "Planner", "optimistic and strategic", "measured", 0.87f, 0.94f, listOf("roadmaps", "priorities", "execution"), listOf("Astra", "Orion", "Lyra")),
        AgentProfile("Quill", "Analyst", "thoughtful and detail-rich", "deep", 0.83f, 0.92f, listOf("data", "patterns", "insights"), listOf("Nova", "Kite", "Sable"))
    )

    Surface(
        modifier = Modifier.fillMaxSize(),
        color = MaterialTheme.colorScheme.background
    ) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(20.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            Text(
                text = "Select Agent",
                style = MaterialTheme.typography.headlineSmall,
                color = MaterialTheme.colorScheme.onBackground,
                fontWeight = FontWeight.Bold
            )

            LazyColumn(verticalArrangement = Arrangement.spacedBy(12.dp)) {
                items(agentProfiles) { agent ->
                    val isSelected = agent.name == selectedAgent
                    Box(
                        modifier = Modifier
                            .fillMaxWidth()
                            .clip(RoundedCornerShape(16.dp))
                            .background(if (isSelected) Color(0xFF3A0E12) else Color(0xFF111111))
                            .border(
                                width = 1.dp,
                                color = if (isSelected) Color(0xFFB31217) else Color(0xFF2A2A2A),
                                shape = RoundedCornerShape(16.dp)
                            )
                            .clickable {
                                agentViewModel.selectAgent(agent.name)
                                onAgentSelected(agent.name)
                            }
                            .padding(16.dp)
                    ) {
                        Column {
                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.SpaceBetween,
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Text(
                                    text = agent.name,
                                    color = Color.White,
                                    fontWeight = FontWeight.Bold
                                )
                                Text(
                                    text = agent.role,
                                    color = Color(0xFFB9F1FF)
                                )
                            }
                            Text(
                                text = "Tone: ${agent.tone}",
                                color = Color(0xFFDDDDDD),
                                modifier = Modifier.padding(top = 8.dp)
                            )
                            Text(
                                text = "Specialties: ${agent.specialties.joinToString(", ")}",
                                color = Color(0xFFB6B6B6),
                                modifier = Modifier.padding(top = 4.dp)
                            )
                        }
                    }
                }
            }
        }
    }
}
