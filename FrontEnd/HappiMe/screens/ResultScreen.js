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

export default class ResultScreen extends React.Component {
  static navigationOptions = {
    title: null,
  };

  constructor(props) {
    super(props);
  }

  render() {

    const {navigation} = this.props;
    const is_unusual = navigation.getParam('is_unusual');

    console.log(is_unusual);

    if (is_unusual == "True") {
        return (
            <View style={{
                flex: 1,
                alignItems: 'center',
                flexDirection: 'column',
                justifyContent: 'center',
                backgroundColor: '#b80f0a'
            }}>
                <Text style={{color: "#FFFFFF", fontSize: 24, fontWeight: "bold"}}> Look's like something's unusual.</Text>
                <Text style={{color: "#FFFFFF", fontSize: 24, fontWeight: "bold"}}> Want us to help out? </Text>
            </View>
        );
    }
    else {
        return (
            <View style={{
                flex: 1,
                alignItems: 'center',
                flexDirection: 'column',
                justifyContent: 'center',
                backgroundColor: '#32CD32'
            }}>
                <Text style={{color: "#FFFFFF", fontSize: 24, fontWeight: "bold"}}> Nothing out of the ordinary here.</Text>
                <Text style={{color: "#FFFFFF", fontSize: 24, fontWeight: "bold"}}> Keep on tracking! </Text>
            </View>
        );
    }

  }
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    flexDirection: 'column',
    justifyContent: 'center',
    backgroundColor: '#32CD32'
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