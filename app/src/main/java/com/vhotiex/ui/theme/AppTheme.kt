package com.vhotiex.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

private val VhotiexDarkColorScheme = darkColorScheme(
    primary = Color(0xFFD32F2F),
    onPrimary = Color.White,
    secondary = Color(0xFFC0C0C0),
    onSecondary = Color(0xFF111111),
    tertiary = Color(0xFFFFFFFF),
    onTertiary = Color(0xFF111111),
    background = Color(0xFF070707),
    onBackground = Color(0xFFFFFFFF),
    surface = Color(0xFF111111),
    onSurface = Color(0xFFFFFFFF),
    surfaceVariant = Color(0xFF1A1A1A),
    onSurfaceVariant = Color(0xFFC7C7C7),
    outline = Color(0xFFB0B0B0),
    error = Color(0xFFB00020),
    onError = Color.White
)

@Composable
fun AppTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = VhotiexDarkColorScheme,
        content = content
    )
}
