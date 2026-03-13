// TODO: Implemente o componente de card de enquete
// Este componente será usado na timeline/feed
//
// Props sugeridas:
// - title: string
// - options: { name: string, votes: number }[]
// - isPublic: boolean
// - createdAt: string
// - onVote: (optionId: number) => void

function PollCard() {
  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h3 className="text-lg font-semibold text-gray-900">
        Título da Enquete
      </h3>
      <p className="text-sm text-gray-500 mt-1">
        Componente de exemplo — substitua pela implementação real
      </p>
    </div>
  )
}

export default PollCard
