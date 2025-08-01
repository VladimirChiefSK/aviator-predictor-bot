package com.example.aviatorpredictor

import android.os.Bundle
import android.os.Handler
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.aviatorpredictor.ui.theme.AviatorPredictorTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            AviatorPredictorTheme {
                SplashScreen()
            }
        }
    }
}

@Composable
fun SplashScreen() {
    var splashVisible by remember { mutableStateOf(true) }
    Handler().postDelayed({ splashVisible = false }, 2000) // 2 seconds splash screen

    if (splashVisible) {
        Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
            Icon(painter = painterResource(id = R.drawable.plane_icon), contentDescription = "Aviator Predictor", tint = Color.White)
        }
    } else {
        MainScreen()
    }
}

@Composable
fun MainScreen() {
    var historyInput by remember { mutableStateOf("") }
    var prediction by remember { mutableStateOf("Prediction: ?") }
    Column(modifier = Modifier.fillMaxSize().padding(16.dp), horizontalAlignment = Alignment.CenterHorizontally) {
        TextField(
            value = historyInput,
            onValueChange = { historyInput = it },
            label = { Text("Enter last multipliers") },
            modifier = Modifier.fillMaxWidth()
        )
        Spacer(modifier = Modifier.height(16.dp))
        Button(onClick = {
            prediction = "Prediction: ${(1..5).random() * 1.0}x"
        }) {
            Text("Predict Next")
        }
        Spacer(modifier = Modifier.height(16.dp))
        Text(text = prediction, style = MaterialTheme.typography.h5, color = Color.Green)
    }
}

@Preview(showBackground = true)
@Composable
fun DefaultPreview() {
    AviatorPredictorTheme {
        MainScreen()
    }
}