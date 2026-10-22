package com.vhotiex.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.vhotiex.ui.agents.AgentSelectorScreen
import com.vhotiex.ui.chat.ChatScreen
import com.vhotiex.ui.settings.SettingsScreen

@Composable
fun NavigationHost() {
    val navController = rememberNavController()

    NavHost(
        navController = navController,
        startDestination = AppRoute.Chat.route
    ) {
        composable(AppRoute.Chat.route) {
            ChatScreen()
        }
        composable(AppRoute.AgentSelector.route) {
            AgentSelectorScreen()
        }
        composable(AppRoute.Settings.route) {
            SettingsScreen()
        }
    }
}
