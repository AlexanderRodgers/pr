import * as firebase from 'firebase/app'
import 'firebase/auth'
import 'firebase/firestore'
import 'firebase/database'

var firebaseConfig = {
    apiKey: "AIzaSyDcS8tNrdd0hh-vv2j9Wlo2bfy_WQyEm5E",
    authDomain: "polyratings-a6a0c.firebaseapp.com",
    databaseURL: "https://polyratings-a6a0c.firebaseio.com",
    projectId: "polyratings-a6a0c",
    storageBucket: "polyratings-a6a0c.appspot.com",
    messagingSenderId: "969495627378",
    appId: "1:969495627378:web:2e1cbb558c25f923"
  };

!firebase.apps.length ? firebase.initializeApp(config) : ''
export const GoogleProvider = new firebase.auth.GoogleAuthProvider()
export const auth = firebase.auth()
export const DB = firebase.database()
export const StoreDB = firebase.firestore()
export default firebase