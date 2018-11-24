import React from 'react';
import {
  Image,
  Platform,
  ScrollView,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
  Button,
  Alert
} from 'react-native';
import { WebBrowser } from 'expo';

import { MonoText } from '../components/StyledText';
import { createStackNavigator, createAppContainer } from 'react-navigation';

export default class HomeScreen extends React.Component {
  static navigationOptions = {
    header: null,
  };

  constructor(props, context) {
    super(props, context);
  }

  render() {
    return (
      <View style={styles.container}>

      <View style={{
        borderBottomColor: "#252627",
        borderBottomWidth: 1,
        marginBottom: 150 }}>
        <Text style={{
            color: "#252627", 
            fontWeight: "bold"}}>How are you feeling today?</Text>
      </View>

        <TouchableOpacity
          onPress={() => {this.props.navigation.navigate('Locations')}}
        > 
          <View style={{
            alignItems: 'center', 
            justifyContent: 'center', 
            borderRadius: 20, 
            height: 50, 
            width: 300, 
            backgroundColor: "#FFFFFF",
            borderColor: "#4B88A2",
            borderWidth: 1,
            marginBottom: 15}}>
            <Text style={{color: "#4B88A2", fontWeight: "bold"}}>Happy</Text>
          </View>
        </TouchableOpacity>

        <TouchableOpacity
          onPress={() => {this.props.navigation.navigate('Locations')}}
        >
          <View style={{
            alignItems: 'center', 
            justifyContent: 'center', 
            borderRadius: 20, 
            height: 50, 
            width: 300, 
            backgroundColor: "#FFFFFF",
            borderColor: "#4B88A2",
            borderWidth: 1,
            marginBottom: 15}}>
            <Text style={{color: "#4B88A2", fontWeight: "bold"}}>Neutral</Text>
          </View>
        </TouchableOpacity>

        <TouchableOpacity
          onPress={() => {this.props.navigation.navigate('Locations')}}
        >
          <View style={{
            alignItems: 'center', 
            justifyContent: 'center', 
            borderRadius: 20, 
            height: 50, 
            width: 300, 
            backgroundColor: "#FFFFFF",
            borderColor: "#4B88A2",
            borderWidth: 1,
            marginBottom: 15}}>
            <Text style={{color: "#4B88A2", fontWeight: "bold"}}>Sad</Text>
          </View>
        </TouchableOpacity>
      </View>

      // <View style={styles.container}>
      //   <ScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
      //     {/* <View style={styles.welcomeContainer}>
      //       <Image
      //         // source={
      //         //   __DEV__
      //         //     ? require('../assets/images/robot-dev.png')
      //         //     : require('../assets/images/robot-prod.png')
      //         // }
      //         style={styles.welcomeImage}
      //       />
      //     </View> */}

      //     <View style={styles.getStartedContainer}>
      //       {/* {this._maybeRenderDevelopmentModeWarning()}

      //       <Text style={styles.getStartedText}>Get started by opening</Text>

      //       <View style={[styles.codeHighlightContainer, styles.homeScreenFilename]}>
      //         <MonoText style={styles.codeHighlightText}>screens/HomeScreen.js</MonoText>
      //       </View> */}

      //       {/* <Text style={styles.getStartedText}>
      //         Hello, welcome to HappiMe.
      //       </Text> */}

      //       <Button
      //         title="Happy"
      //         color="#841584"
      //         accessibilityLabel="Happy"
      //         onPress={() => {this.props.navigation.navigate('Details')}}
      //       />

      //       <Button
      //         title="Neutral"
      //         color="#841584"
      //         accessibilityLabel="Happy"
      //         onPress={() => {this.props.navigation.navigate('Details')}}
      //       />

      //       <Button
      //         title="Sad"
      //         color="#841584"
      //         accessibilityLabel="Happy"
      //         onPress={() => {this.props.navigation.navigate('Details')}}
      //         style={styles.buttonCenter}
      //       />

      //     </View>

      //     {/* <View style={styles.helpContainer}>
      //       <TouchableOpacity onPress={this._handleHelpPress} style={styles.helpLink}>
      //         <Text style={styles.helpLinkText}>Help, it didn’t automatically reload!</Text>
      //       </TouchableOpacity>
      //     </View> */}
      //   </ScrollView>

      //   {/* <View style={styles.tabBarInfoContainer}>
      //     <Text style={styles.tabBarInfoText}>This is a tab bar. You can edit it in:</Text>

      //     <View style={[styles.codeHighlightContainer, styles.navigationFilename]}>
      //       <MonoText style={styles.codeHighlightText}>navigation/MainTabNavigator.js</MonoText>
      //     </View>
      //   </View> */}
      // </View>
    );
  }

  _maybeRenderDevelopmentModeWarning() {
    if (__DEV__) {
      const learnMoreButton = (
        <Text onPress={this._handleLearnMorePress} style={styles.helpLinkText}>
          Learn more
        </Text>
      );

      return (
        <Text style={styles.developmentModeText}>
          Development mode is enabled, your app will be slower but you can use useful development
          tools. {learnMoreButton}
        </Text>
      );
    } else {
      return (
        <Text style={styles.developmentModeText}>
          You are not in development mode, your app will run at full speed.
        </Text>
      );
    }
  }

  _handleLearnMorePress = () => {
    WebBrowser.openBrowserAsync('https://docs.expo.io/versions/latest/guides/development-mode');
  };

  _handleHelpPress = () => {
    WebBrowser.openBrowserAsync(
      'https://docs.expo.io/versions/latest/guides/up-and-running.html#can-t-see-your-changes'
    );
  };
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    flexDirection: 'column',
    justifyContent: 'center',
    backgroundColor: '#FFFFFF'
  },
  buttonContainer: {
    paddingLeft: 50,
    paddingRight: 50,
    flex: 1
  },
  moodBtn: {
    backgroundColor: '#dfe6e9',
    borderRadius: 10,
    flex: 0.8,
    height: 30
  },
  spacer: {
    height: 20
  }
});



// buttonCenter: {
//   justifyContent: 'center',
//   alignItems: 'center',
//   alignSelf: 'center'
// },
// container: {
//   flex: 1,
//   backgroundColor: '#fff',
// },
// developmentModeText: {
//   marginBottom: 20,
//   color: 'rgba(0,0,0,0.4)',
//   fontSize: 14,
//   lineHeight: 19,
//   textAlign: 'center',
// },
// contentContainer: {
//   paddingTop: 30,
// },
// welcomeContainer: {
//   alignItems: 'center',
//   marginTop: 10,
//   marginBottom: 20,
// },
// welcomeImage: {
//   width: 100,
//   height: 80,
//   resizeMode: 'contain',
//   marginTop: 3,
//   marginLeft: -10,
// },
// getStartedContainer: {
//   alignItems: 'center',
//   flex: 1,
//   justifyContent: 'center',
//   marginHorizontal: 50,
// },
// homeScreenFilename: {
//   marginVertical: 7,
// },
// codeHighlightText: {
//   color: 'rgba(96,100,109, 0.8)',
// },
// codeHighlightContainer: {
//   backgroundColor: 'rgba(0,0,0,0.05)',
//   borderRadius: 3,
//   paddingHorizontal: 4,
// },
// getStartedText: {
//   fontSize: 17,
//   color: 'rgba(96,100,109, 1)',
//   lineHeight: 24,
//   textAlign: 'center',
// },
// tabBarInfoContainer: {
//   position: 'absolute',
//   bottom: 0,
//   left: 0,
//   right: 0,
//   ...Platform.select({
//     ios: {
//       shadowColor: 'black',
//       shadowOffset: { height: -3 },
//       shadowOpacity: 0.1,
//       shadowRadius: 3,
//     },
//     android: {
//       elevation: 20,
//     },
//   }),
//   alignItems: 'center',
//   backgroundColor: '#fbfbfb',
//   paddingVertical: 20,
// },
// tabBarInfoText: {
//   fontSize: 17,
//   color: 'rgba(96,100,109, 1)',
//   textAlign: 'center',
// },
// navigationFilename: {
//   marginTop: 5,
// },
// helpContainer: {
//   marginTop: 15,
//   alignItems: 'center',
// },
// helpLink: {
//   paddingVertical: 15,
// },
// helpLinkText: {
//   fontSize: 14,
//   color: '#2e78b7',
// },