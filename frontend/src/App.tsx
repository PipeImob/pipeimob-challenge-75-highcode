import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import LoginPage from './pages/LoginPage'

// TODO: Implemente suas rotas aqui
// Sugestão de rotas:
// /login - Página de login
// /register - Página de cadastro
// /polls - Timeline de enquetes (rota protegida)
// /polls/:id - Detalhes de uma enquete (rota protegida)

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="*" element={<Navigate to="/login" replace />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
