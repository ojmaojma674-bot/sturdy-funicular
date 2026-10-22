package com.vhotiex.ui.chat

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Send
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import com.vhotiex.model.ChatMessage

private data class AgentChip(
    val name: String,
    val role: String,
    val accent: Color
)

@Composable
fun ChatScreen(
    chatViewModel: ChatViewModel = viewModel(),
    agentViewModel: com.vhotiex.ui.agents.AgentViewModel = viewModel(),
    onOpenAgents: () -> Unit = {}
) {
    val messages by chatViewModel.messages.collectAsState()
    val selectedAgent by agentViewModel.selectedAgent.collectAsState()
    var draft by remember { mutableStateOf("") }

    val agentChips = listOf(
        AgentChip("Astra", "Coordinator", MaterialTheme.colorScheme.primary),
        AgentChip("Nova", "Research", Color(0xFFB7B7B7)),
        AgentChip("Orion", "Engineering", Color(0xFFF0F0F0)),
        AgentChip("Lyra", "Creative", Color(0xFFDEDEDE)),
        AgentChip("Echo", "Voice", Color(0xFFD9D9D9))
    )

    Surface(
        modifier = Modifier.fillMaxSize(),
        color = MaterialTheme.colorScheme.background
    ) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .background(
                    brush = Brush.verticalGradient(
                        listOf(
                            Color(0xFF070707),
                            Color(0xFF0F0F0F),
                            Color(0xFF161616)
                        )
                    )
                )
                .padding(horizontal = 18.dp, vertical = 20.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Column {
                    Text(
                        text = "VHOTIEX AI",
                        style = MaterialTheme.typography.headlineMedium,
                        fontWeight = FontWeight.Bold,
                        color = Color.White
                    )
                    Text(
                        text = "mission control for your AI team",
                        color = MaterialTheme.colorScheme.onSurfaceVariant
                    )
                }

                Box(
                    modifier = Modifier
                        .clip(RoundedCornerShape(999.dp))
                        .background(Color(0xFF2A0B0D))
                        .padding(horizontal = 12.dp, vertical = 8.dp)
                ) {
                    Text(
                        text = "Online",
                        color = Color(0xFFF3F3F3),
                        fontWeight = FontWeight.SemiBold
                    )
                }
            }

            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.spacedBy(10.dp)
            ) {
                StatCard(title = "Agents", value = "5", tone = MaterialTheme.colorScheme.primary)
                StatCard(title = "Tasks", value = "12", tone = Color(0xFFB0B0B0))
                StatCard(title = "Voice", value = "96%", tone = Color(0xFFFFFFFF))
            }

            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .clip(RoundedCornerShape(18.dp))
                    .background(Color(0xFF111111))
                    .border(1.dp, Color(0xFF3B3B3B), RoundedCornerShape(18.dp))
                    .padding(16.dp)
            ) {
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceBetween,
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Column {
                        Text(
                            text = "Selected agent",
                            color = Color(0xFFB9B9B9)
                        )
                        Text(
                            text = selectedAgent,
                            color = Color.White,
                            fontWeight = FontWeight.Bold,
                            modifier = Modifier.padding(top = 4.dp)
                        )
                    }
                    Button(
                        onClick = onOpenAgents,
                        colors = ButtonDefaults.buttonColors(containerColor = MaterialTheme.colorScheme.primary)
                    ) {
                        Text("Switch")
                    }
                }
            }

            LazyRow(
                horizontalArrangement = Arrangement.spacedBy(10.dp),
                modifier = Modifier.fillMaxWidth()
            ) {
                items(agentChips) { chip ->
                    val selected = chip.name == selectedAgent
                    Box(
                        modifier = Modifier
                            .clip(RoundedCornerShape(14.dp))
                            .background(if (selected) chip.accent.copy(alpha = 0.18f) else Color(0xFF141414))
                            .border(
                                width = 1.dp,
                                color = if (selected) chip.accent else Color(0xFF2B2B2B),
                                shape = RoundedCornerShape(14.dp)
                            )
                            .clickable { agentViewModel.selectAgent(chip.name) }
                            .padding(horizontal = 14.dp, vertical = 10.dp)
                    ) {
                        Column {
                            Text(
                                text = chip.name,
                                color = Color.White,
                                fontWeight = FontWeight.Bold
                            )
                            Text(
                                text = chip.role,
                                color = Color(0xFFCECECE),
                                modifier = Modifier.padding(top = 2.dp)
                            )
                        }
                    }
                }
            }

            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .weight(1f)
                    .clip(RoundedCornerShape(22.dp))
                    .background(Color(0xFF151515))
                    .border(1.dp, Color(0xFF3C3C3C), RoundedCornerShape(22.dp))
                    .padding(12.dp)
            ) {
                LazyColumn(
                    verticalArrangement = Arrangement.spacedBy(10.dp),
                    modifier = Modifier.fillMaxSize()
                ) {
                    items(messages) { message ->
                        MessageBubble(message = message)
                    }
                }
            }

            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.spacedBy(10.dp),
                verticalAlignment = Alignment.Bottom
            ) {
                OutlinedTextField(
                    value = draft,
                    onValueChange = { draft = it },
                    modifier = Modifier
                        .weight(1f)
                        .heightIn(min = 56.dp),
                    placeholder = { Text("Ask the team...") },
                    shape = RoundedCornerShape(18.dp),
                    textStyle = androidx.compose.ui.text.TextStyle(color = Color.White)
                )

                Button(
                    onClick = {
                        chatViewModel.sendMessage(draft.trim(), selectedAgent)
                        draft = ""
                    },
                    enabled = draft.isNotBlank(),
                    colors = ButtonDefaults.buttonColors(containerColor = MaterialTheme.colorScheme.primary)
                ) {
                    Icon(Icons.Default.Send, contentDescription = "Send")
                }
            }
        }
    }
}

@Composable
private fun StatCard(title: String, value: String, tone: Color) {
    Box(
        modifier = Modifier
            .weight(1f)
            .clip(RoundedCornerShape(14.dp))
            .background(Color(0xFF111111))
            .border(1.dp, Color(0xFF333333), RoundedCornerShape(14.dp))
            .padding(vertical = 12.dp, horizontal = 14.dp)
    ) {
        Column {
            Text(
                text = title,
                color = Color(0xFFC7C7C7),
                fontWeight = FontWeight.Medium
            )
            Text(
                text = value,
                color = tone,
                fontWeight = FontWeight.Bold,
                modifier = Modifier.padding(top = 6.dp)
            )
        }
    }
}

@Composable
private fun MessageBubble(message: ChatMessage) {
    val bubbleColor = if (message.isUser) MaterialTheme.colorScheme.primary else Color(0xFF1C1C1C)
    val textColor = if (message.isUser) Color.White else Color(0xFFF3F3F3)
    val alignment = if (message.isUser) Alignment.End else Alignment.Start

    Box(
        modifier = Modifier.fillMaxWidth(),
        contentAlignment = alignment
    ) {
        Column(
            modifier = Modifier
                .clip(RoundedCornerShape(16.dp))
                .background(bubbleColor)
                .padding(horizontal = 14.dp, vertical = 12.dp)
        ) {
            Text(
                text = if (message.isUser) "You" else message.sender,
                color = if (message.isUser) Color(0xFFE7DADA) else Color(0xFFB9F1FF),
                fontWeight = FontWeight.SemiBold
            )
            Text(
                text = message.text,
                color = textColor,
                modifier = Modifier.padding(top = 4.dp)
            )
        }
    }
}
