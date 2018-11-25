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

    this.sendTextMessage = this.sendTextMessage.bind(this);
  }

    sendTextMessage(data) {

        let setup = {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        }

        fetch('https://utils.lib.id/sms@1.0.9/', setup)
        .then(response => response.json())
        .then(responseData => {

            console.log(responseData);

            if (responseData['status'] == "sent") {
                
            } else {
                Alert.alert("Something went wrong.");
            }

        });

    }

  render() {

    const {navigation} = this.props;
    const is_unusual = navigation.getParam('is_unusual');

    if (is_unusual == "True") {

        var data = {
            "to": "5192164264",
            "body": "Look's like your friend Jonathan is feeling down, you should send a message."
        }

        this.sendTextMessage(data);

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