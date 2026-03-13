// TODO: Implemente o client HTTP para comunicação com o backend
// Sugestões:
// - Usar fetch ou axios
// - Configurar base URL
// - Adicionar interceptor para token JWT
// - Tratar erros de forma consistente

const API_BASE_URL = import.meta.env.VITE_API_URL || '/api/v1'

export async function apiRequest(endpoint: string, options: RequestInit = {}) {
  const url = `${API_BASE_URL}${endpoint}`

  // TODO: Adicionar token JWT nos headers
  const headers: HeadersInit = {
    'Content-Type': 'application/json',
    ...options.headers,
  }

  const response = await fetch(url, { ...options, headers })

  if (!response.ok) {
    // TODO: Tratar erros de forma mais robusta
    const error = await response.json().catch(() => ({ detail: 'Erro desconhecido' }))
    throw new Error(error.detail || `HTTP ${response.status}`)
  }

  return response.json()
}
