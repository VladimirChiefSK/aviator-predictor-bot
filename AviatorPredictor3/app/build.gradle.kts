plugins {
    id 'com.android.application'
    id 'org.jetbrains.kotlin.android'
}

android {
    compileSdk 34

    defaultConfig {
        applicationId "com.example.aviatorpredictor"
        minSdk 26
        targetSdk 34
        versionCode 1
        versionName "1.0"
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }

    composeOptions {
        kotlinCompilerExtensionVersion "1.4.0"
        kotlinCompilerVersion "1.9.0"
    }
}

dependencies {
    implementation 'androidx.compose.ui:ui:1.4.0'
    implementation 'androidx.compose.material3:material3:1.0.0'
    implementation 'androidx.compose.ui:ui-tooling-preview:1.4.0'
    implementation 'androidx.lifecycle:lifecycle-runtime-ktx:2.5.1'
    implementation 'com.github.mikephil.charting:MPAndroidChart:3.1.0'
    implementation 'androidx.activity:activity-compose:1.6.1'
    debugImplementation 'androidx.compose.ui:ui-tooling:1.4.0'
}