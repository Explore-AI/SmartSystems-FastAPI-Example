import React, { useState, useEffect} from "react";
import AuthProvider from './hocs/AuthProvider'
import { getActiveMsalAccount, logout } from "./lib/AuthUtils";
import Accounts from "./components/Accounts/Accounts"
import AppNavigationBar from "./components/navigation/NavBar";
import { blueGrey } from '@mui/material/colors';
import { createTheme, ThemeProvider } from '@mui/material/styles'


const App = () => {
	const [userId, setUserId] = useState(null);
	const [name, setName] = useState(null);
	const [displayName, setDisplayName] = useState(null);
	
	const darkTheme = createTheme({
		palette: {
		  mode: 'light',
		  primary: {
			main: blueGrey[500],
		  },
		},
	});

	const handleLogOff = () => {
		console.log('logging out...');
		logout();
	}

	useEffect(() => {

		let user = getActiveMsalAccount();
		setDisplayName(user.username);
		setName(user.name);
		setUserId(user.homeAccountId);
		
	}, []);

	return (
		<div>
			<ThemeProvider theme={darkTheme}>
				<AppNavigationBar logout = {handleLogOff}  activeUser = {{userId:userId, displayName:displayName,name:name}}/>
				<div className="center">
					<Accounts/>
				</div>
			</ThemeProvider>
		</div>
	);
}

export default AuthProvider(App);