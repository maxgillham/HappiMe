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

export default class LocationScreen extends React.Component {
  static navigationOptions = {
    title: null,
  };

  render() {
    return (
      <View style={styles.container}>

      <View style={{
        borderBottomColor: "#252627",
        borderBottomWidth: 1,
        marginBottom: 75 }}>
        <Text style={{
            color: "#252627", 
            fontWeight: "bold"}}>Where did you spend your day?</Text>
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
            <Text style={{color: "#4B88A2", fontWeight: "bold"}}>Home</Text>
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
            <Text style={{color: "#4B88A2", fontWeight: "bold"}}>Gym</Text>
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
            <Text style={{color: "#4B88A2", fontWeight: "bold"}}>Class</Text>
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
            <Text style={{color: "#4B88A2", fontWeight: "bold"}}>Library</Text>
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
            <Text style={{color: "#4B88A2", fontWeight: "bold"}}>Bar</Text>
          </View>
        </TouchableOpacity>
      </View>
    );
  }
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