package com.vhotiex.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

private val VhotiexDarkColorScheme = darkColorScheme(
    primary = Color(0xFFB31217),
    secondary = Color(0xFF6A0D1B),
    tertiary = Color(0xFF00D1FF),
    background = Color(0xFF090909),
    surface = Color(0xFF111111),
    onPrimary = Color.White,
    onSecondary = Color.White,
    onBackground = Color.White,
    onSurface = Color.White
)

@Composable
fun AppTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = VhotiexDarkColorScheme,
        content = content
    )
}
