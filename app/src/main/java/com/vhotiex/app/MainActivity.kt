package com.vhotiex.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import com.vhotiex.ui.theme.AppTheme
import com.vhotiex.ui.chat.ChatScreen

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            AppTheme {
                ChatScreen()
            }
        }
    }
}
