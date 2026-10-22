package com.vhotiex.navigation

import androidx.compose.runtime.Composable
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.vhotiex.ui.agents.AgentSelectorScreen
import com.vhotiex.ui.agents.AgentViewModel
import com.vhotiex.ui.chat.ChatScreen
import com.vhotiex.ui.chat.ChatViewModel
import com.vhotiex.ui.settings.SettingsScreen

@Composable
fun NavigationHost() {
    val navController = rememberNavController()
    val chatViewModel: ChatViewModel = viewModel()
    val agentViewModel: AgentViewModel = viewModel()

    NavHost(
        navController = navController,
        startDestination = AppRoute.Chat.route
    ) {
        composable(AppRoute.Chat.route) {
            ChatScreen(
                chatViewModel = chatViewModel,
                agentViewModel = agentViewModel,
                onOpenAgents = { navController.navigate(AppRoute.AgentSelector.route) }
            )
        }
        composable(AppRoute.AgentSelector.route) {
            AgentSelectorScreen(
                agentViewModel = agentViewModel,
                onAgentSelected = {
                    navController.popBackStack()
                }
            )
        }
        composable(AppRoute.Settings.route) {
            SettingsScreen()
        }
    }
}
