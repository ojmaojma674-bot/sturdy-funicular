package com.vhotiex.navigation

sealed class AppRoute(val route: String) {
    data object Chat : AppRoute("chat")
    data object AgentSelector : AppRoute("agent_selector")
    data object Settings : AppRoute("settings")
}
