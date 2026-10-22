package com.vhotiex.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable

private val VhotiexDarkColorScheme = darkColorScheme(
    primary = androidx.compose.ui.graphics.Color(0xFFB31217),
    secondary = androidx.compose.ui.graphics.Color(0xFF6A0D1B),
    tertiary = androidx.compose.ui.graphics.Color(0xFF00D1FF),
    background = androidx.compose.ui.graphics.Color(0xFF090909),
    surface = androidx.compose.ui.graphics.Color(0xFF111111),
    onPrimary = androidx.compose.ui.graphics.Color.White,
    onSecondary = androidx.compose.ui.graphics.Color.White,
    onBackground = androidx.compose.ui.graphics.Color.White,
    onSurface = androidx.compose.ui.graphics.Color.White
)

@Composable
fun AppTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = VhotiexDarkColorScheme,
        content = content
    )
}
