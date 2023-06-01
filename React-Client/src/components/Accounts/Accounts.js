/** @jsxRuntime classic */
/** @jsx jsx */
import { jsx, css } from "@emotion/react";
import { useState, useEffect, Suspense } from "react";
import { get, map, trim, size } from "lodash";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";
import EditIcon from "@mui/icons-material/Edit";
import CircularProgress from "@mui/material/CircularProgress";
import { getUsers, updateUser } from "../../helpers/services/TestServices";
import Typography from "@mui/material/Typography";
import Modal from "@mui/material/Modal";
import Box from "@mui/material/Box";

const Accounts = () => {
  const [users, setUsers] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [invalid, setInvalid] = useState({});
  const [newUser, setNewUser] = useState({});

  const [open, setOpen] = useState(false);
  const handleOpenModal = () => setOpen(true);
  const handleCloseModal = () => setOpen(false);

  useEffect(() => {
    getUserDetail();
  }, []);

  const getUserDetail = () => {
    setIsLoading(true);
    getUsers().then((response) => {
      setUsers(response);
      setIsLoading(false);
    });
  };

  const setValue = (e) => {
    setNewUser({ ...newUser, [get(e, "target.name")]: get(e, "target.value") });
    if (trim(get(e, "target.value")) !== "") {
      setInvalid({ ...invalid, [get(e, "target.name")]: false });
    }
  };

  const updateSelectedUser = () => {
    let validate = {};

    if (!trim(get(newUser, "Id"))) {
      validate.Id = true;
    }
    if (!trim(get(newUser, "username"))) {
      validate.username = true;
    }
    if (!trim(get(newUser, "email"))) {
      validate.email = true;
    }

    if (size(validate)) {
      setInvalid(validate);
      return;
    }
    handleCloseModal();
    setIsLoading(true);
    updateUser(newUser).then((response) => {
      if (get(response, "UserId")) {
        setNewUser({});
        setInvalid({});
        getUserDetail();
      } else {
        console.log("Error");
      }
    });
  };

  const setEditVal = (row) => {
    handleOpenModal();
    setInvalid({});
    setNewUser({
      Id: get(row, "UserId"),
      username: get(row, "UserName"),
      email: get(row, "Email"),
    });
  };

  return (
    <div css={testContainer}>
      <Modal
        open={open}
        onClose={handleCloseModal}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={modalstyle}>
          <Typography id="modal-modal-title" variant="h6" component="div">
            <h2>UPDATE USER</h2>
          </Typography>

          <Typography id="modal-modal-description">
            <Stack spacing={3} direction="row">
              <TextField
                id="outlined-controlled"
                label="Name"
                name="username"
                value={get(newUser, "username", "")}
                autoComplete="off"
                error={get(invalid, "username") ? true : false}
                onChange={(e) => setValue(e)}
              />
              <TextField
                id="outlined-controlled"
                label="Email"
                name="email"
                value={get(newUser, "email", "")}
                autoComplete="off"
                error={get(invalid, "email") ? true : false}
                onChange={(e) => setValue(e)}
              />
              <Button
                variant="contained"
                disabled={!get(newUser, "Id") ? true : false}
                style={{ color: "orange" }}
                onClick={() => updateSelectedUser()}
              >
                Update
              </Button>
              <Button
                variant="outlined"
                style={{ color: "red" }}
                onClick={() => handleCloseModal()}
              >
                Close
              </Button>
            </Stack>
          </Typography>
        </Box>
      </Modal>

      <div className="tableContainer">
        <h1>Accounts</h1>
        {isLoading ? (
          <div className="loading">
            <CircularProgress />
          </div>
        ) : (
          <Suspense fallback={<p>Loading...</p>}>
            <TableContainer component={Paper}>
              <Table
                sx={{ minWidth: 650 }}
                size="small"
                aria-label="a dense table"
              >
                <TableHead>
                  <TableRow>
                    <TableCell>Id</TableCell>
                    <TableCell>Name</TableCell>
                    <TableCell>Email</TableCell>
                    <TableCell align="right">Edit</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {map(users, (row, key) => {
                    return (
                      <TableRow
                        key={key}
                        sx={{
                          "&:last-child td, &:last-child th": { border: 0 },
                        }}
                      >
                        <TableCell component="th" scope="row">
                          {get(row, "UserId")}
                        </TableCell>
                        <TableCell>{get(row, "UserName")}</TableCell>
                        <TableCell>{get(row, "Email")}</TableCell>
                        <TableCell align="right">
                          <EditIcon
                            className="pointer"
                            onClick={() => setEditVal(row)}
                          />
                        </TableCell>
                      </TableRow>
                    );
                  })}
                </TableBody>
              </Table>
            </TableContainer>
          </Suspense>
        )}
      </div>
    </div>
  );
};

export default Accounts;

const testContainer = css`
  margin-left: 20%;
  text-align: center;
  align-content: center;

  & .tableContainer {
    padding: 10px;
    max-width: 60%;
    & .loading {
      text-align: center;
    }
    & .pointer {
      cursor: pointer;
    }
  }
`;

const modalstyle = {
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: 700,
  bgcolor: "background.paper",
  border: "2px solid #607d8b",
  boxShadow: 24,
  p: 4,
  borderRadius: 5,
};
